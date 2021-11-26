<?php
session_start();

require_once "conexao.php";

if($_SESSION["isAdmin"] != true){
	header("Location: /index.php");
}

$conexao = new Conexao();
$banco = $conexao->getCon();

if(isset($_POST["criar"]) && isset($_POST["icone"]) && isset($_POST["titulo"]) && !empty($_POST["titulo"])){
	$icone = $_POST["icone"];
	$titulo = $_POST["titulo"];
	$id = $_POST["id"];
	
	$sql = "INSERT INTO artigo (forum, icone, titulo) values (:id, :icone, :titulo)";
	$set = $banco->prepare($sql);
	$set->bindValue(":id", $id);
	$set->bindValue(":icone", $icone);
	$set->bindValue(":titulo", $titulo);
	$set->execute();
}

if (isset($_GET["delete"]) && isset($_GET["id"])){
	$id = $_GET["id"];
	$sql = "DELETE FROM artigo WHERE id = :id";
	$del = $banco->prepare($sql);
	$del->bindValue(":id", $id);
	$del->execute();
}


$banco = null;
header("Location: /index.php");

?>