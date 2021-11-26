<?php
session_start();

require_once "/sistema/config.php";
require_once "/sistema/conexao.php";

$conexao = new Conexao();
$banco = $conexao->getCon();

if(isset($_GET["post"])){
	$sql = "SELECT * FROM artigos WHERE titulo = :post";
	$get = $banco->prepare($sql);
	$get->bindValue(":post", $_GET["post"]);
	$get->execute();
	$post = $get->fetch(PDO::FETCH_ASSOC);
} else {
	header("Location: index.php");
}

if (!isset($post) || empty($post)) {
	header("Location: index.php");
}

$sql = "SELECT * FROM users WHERE playerid = :usuarioid";
$get = $banco->prepare($sql);
$get->bindValue(":usuarioid", $post["usuarioid"]);
$get->execute();
$usuario = $get->fetch(PDO::FETCH_ASSOC);

$img = "http://avatars.atelier801.com/". $usuario["avatar"] % 10000 ."/".$usuario["avatar"].".jpg";

?>
<!DOCTYPE html>
<html>
	<head>
		<link rel="stylesheet" type="text/css" href="/css/main.css">
		<link rel="stylesheet" type="text/css" href="/css/forum.css">
		<link rel="stylesheet" type="text/css" href="/css/artigo.css">
		<meta charset="utf-8">
		<title><?php echo $post["titulo"]; ?></title>
	</head>
	<body>

		<div class="header">
			<header>
				<div class="linha">
					<div class="col col2 voarE">
						<h2><a href="/index.php" class="titulo">MaiceMice</a></h2>
					</div>

					<div class="col col5 centT voarD">
						<nav>
							<ul class="spaddin slist menuH menuP voarD">
								<li><a href="./ranking.php">Ranking</a></li>
								<?php if (isset($_SESSION["logado"])): ?>
								<li><a href="./configurar.php#config-conta">Configurar</a></li>
								<li><a href="./sair.php">Sair</a></li>
								<?php else: ?>
								<li><a href="./entrar.php">Entrar</a></li>
								<?php endif; ?>
							</ul>
						</nav>
					</div>
				</div>
			</header>
		</div>


		<div class="display-artigo">
			<div class="linha">
				
				<div class="artigotitulo col col10 bg margin bd">
					<h1><?php echo $post["titulo"]; ?></h1>
				</div>
				
				<div class="artigo col col10 bg margin bd">

					<div class="artigo-perfil col col10 over">
						<div class="foto col">
							<img src='<?php echo $img; ?>'>
						</div>
						<div class="info-perfil">
							<h4><?php $nick = explode("#", $usuario["Username"]); echo $nick[0]; ?><span><?php echo "#".$nick[1]; ?></span></h4>
							<span><?php $data = explode("-", $post["data"]); echo "$data[2]/$data[1]/$data[0]"; ?></span>
							<h6><?php echo $rank[$usuario["PrivLevel"]]; ?></h6>
						</div>
					</div>

					<div class="artigo-conteudo centT conteudo col col10">
						<?php echo $post["conteudo"]; ?>
					</div>
				</div>
			</div>
		</div>


	</body>
</html>

<?php

$banco = null;

?>