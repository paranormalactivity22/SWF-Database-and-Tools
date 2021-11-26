<?php
session_start();
date_default_timezone_set('UTC');

require_once "conexao.php";

if($_SESSION["isAdmin"] != true){
	header("Location: /index.php");
}

$conexao = new Conexao();
$banco = $conexao->getCon();

if(isset($_POST["criar"]) && !empty($_POST["titulo"])){
	if(!empty($_POST["forum"]) && !empty($_POST["artigo"])){
		$titulo = $_POST["titulo"];
		$conteudo = $_POST["conteudo"];
		$forum = $_POST["forum"];
		$artigo = $_POST["artigo"];

		$sql = "SELECT PlayerID FROM users WHERE Username = :usuario";
		$get = $banco->prepare($sql);
		$get->bindValue(":usuario", $_SESSION["nick"]);
		$get->execute();
		$usuario = $get->fetch(PDO::FETCH_ASSOC);


		$sql = "INSERT INTO artigos (forumid, artigoid, usuarioid, data, titulo, conteudo) values (:forumid, :artigoid, :usuarioid, :data, :titulo, :conteudo)";
		$set = $banco->prepare($sql);
		$set->bindValue(":forumid", $forum);
		$set->bindValue(":artigoid", $artigo);
		$set->bindValue(":usuarioid", $usuario["PlayerID"]);
		$set->bindValue(":data", date("Y-m-d"));
		$set->bindValue(":titulo", $titulo);
		$set->bindValue(":conteudo", $conteudo);
		$set->execute();

		$sql = "UPDATE artigo SET ultimo = :ultimo WHERE id = :forumid";
		$set = $banco->prepare($sql);
		$set->bindValue(":ultimo", $titulo);
		$set->bindValue(":forumid", $forum);
		$set->execute();

		header("Location: /index.php#/secao.php?f=" . $forum . "&a=" . $artigo);
	}

}

if (isset($_GET["delete"]) && isset($_GET["id"])){
	$id = $_GET["id"];
	$sql = "DELETE FROM artigos WHERE id = :id";
	$del = $banco->prepare($sql);
	$del->bindValue(":id", $id);
	$del->execute();
}


$banco = null;
header("Location: /index.php");
?>