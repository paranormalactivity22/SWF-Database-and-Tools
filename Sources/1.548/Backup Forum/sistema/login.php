<?php

require_once "conexao.php";

Class Login {

	private $banco;

	public function __construct(){
		$conexao = new Conexao();
		$this->banco = $conexao->getCon();
	}

	public function getPassword($nick){

		$sql = "SELECT username, password FROM users WHERE username = :nick";

		$con = $this->banco->prepare($sql);
		$con->bindValue(":nick", $nick);
		$con->execute();

		return $con->fetch(PDO::FETCH_ASSOC);

	}

	public function changePassword($nick, $pass, $newpass){
		$getoldpass = $this->getPassword($nick);
		$oldpass = $getoldpass["password"];
		if ($oldpass == $pass):
			$sql = "UPDATE users SET password = :newpass WHERE username = :nick";
			$con = $this->banco->prepare($sql);
			$con->bindValue(":newpass", $newpass);
			$con->bindValue(":nick", $nick);
			$con->execute();
			return true;
		else:
			return false;
		
		endif;
	}

	public function getEmail($nick){
		$sql = "SELECT Email FROM users WHERE username = :nick";
		$con = $this->banco->prepare($sql);
		$con->bindValue(":nick", $nick);
		$con->execute();
		$dado = $con->fetch(PDO::FETCH_ASSOC);
		return $dado["Email"];
	}

	public function getInfosByNick($nick){
		$sql = "SELECT * FROM users WHERE username = :nick";
		$con = $this->banco->prepare($sql);
		$con->bindValue(":nick", $nick);
		$con->execute();
		$dado = $con->fetch(PDO::FETCH_ASSOC);
		return $dado;
	}

	public function getInfosByID($id){
		$sql = "SELECT * FROM users WHERE playerid = :id";
		$con = $this->banco->prepare($sql);
		$con->bindValue(":id", $id);
		$con->execute();
		$dado = $con->fetch(PDO::FETCH_ASSOC);
		return $dado;
	}

}

?>