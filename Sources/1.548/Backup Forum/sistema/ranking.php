<?php

require_once "conexao.php";

class Ranking {

	public $count;
	private $banco;	

	public function __construct(){
		$conexao = new Conexao();
		$this->banco = $conexao->getCon();
	}

	public function getRankingByName($nick){
		
		$sql = "SELECT username, firstcount, cheesecount, bootcampcount, shamansaves, hardmodesaves, divinemodesaves from Users where username like :nick";

		$get = $this->banco->prepare($sql);
		$get->bindValue(":nick", $nick);
		$get->execute();

		return $get->fetch(PDO::FETCH_ASSOC);

	}

	public function getRanking($rank, $orderby){

		$sql = "SELECT username, firstcount, cheesecount, bootcampcount, shamansaves, hardmodesaves, divinemodesaves from Users where privlevel < :rank order by firstcount DESC";

		$get = $this->banco->prepare($sql);
		$get->bindValue(":rank", $rank);
		//$get->bindValue(":orderby", $orderby);
		$get->execute();

		$this->count = $get->rowCount();

		return $get->fetchAll(PDO::FETCH_ASSOC);

	}

}
?>