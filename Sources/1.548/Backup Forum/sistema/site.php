<?php

require_once "conexao.php";

class Site{

	private $key = "1561561775";
	private $banco;

	public function __construct(){
		$conexao = new Conexao();
		$this->banco = $conexao->getCon();
	}

	public function getInfos(){
		$sql = "SELECT * FROM infosite WHERE chave = :key";
		$get = $this->banco->prepare($sql);
		$get->bindValue(":key", $this->key);
		$get->execute();
		return $get->fetch(PDO::FETCH_ASSOC);
	}

	public function setInfos($ons, $versao){
		$infos = $this->getInfos($this->key);
		$recorde_antigo = $infos["recorde"];
		$recorde = ($recorde_antigo < $ons) ? $ons : $recorde_antigo;
		$sql = "UPDATE infosite SET onlines = :ons, recorde = :rec, versao = :ver WHERE chave = :key";
		$set = $this->banco->prepare($sql);
		$set->bindValue(":ons", (int)$ons);
		$set->bindValue(":rec", (int)$recorde);
		$set->bindValue(":ver", (int)$versao);
		$set->bindValue(":key", (int)$this->key);		
		$set->execute();
	}
}

?>