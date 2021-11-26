<?php
session_start();

require_once "/sistema/config.php";
require_once("/sistema/conexao.php");

$conexao = new Conexao();
$banco = $conexao->getCon();

if(isset($_GET["f"]) && isset($_GET["a"])){
	$sql = "SELECT * FROM artigos WHERE forumid = :fid and artigoid = :aid";
	$get = $banco->prepare($sql);
	$get->bindValue(":fid", $_GET["f"]);
	$get->bindValue(":aid", $_GET["a"]);
	$get->execute();
	$secoes = $get->fetchAll(PDO::FETCH_ASSOC);
}

?>
<!DOCTYPE html>
<html lang="pt-br">
	<head>
		<link rel="stylesheet" type="text/css" href="/css/main.css">
		<link rel="stylesheet" type="text/css" href="/css/forum.css">
		<link rel="stylesheet" type="text/css" href="/css/secao.css">
		<link rel="icon" type="images/png" href="/img/favicon.png" />
		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
		<title>Forum - MaiceMice</title>
		<meta charset="utf-8">
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
								<li><a href="/ranking.php">Ranking</a></li>
								<?php if (isset($_SESSION["logado"])): ?>
								<li><a href="/configurar.php#config-conta">Configurar</a></li>
								<li><a href="/sair.php">Sair</a></li>
								<?php else: ?>
								<li><a href="/entrar.php">Entrar</a></li>
								<?php endif; ?>
							</ul>
						</nav>
					</div>
				</div>
			</header>
		</div>


		<div class="secoes">
			<div class="linha">
				<div class="secoes col col9 centC">
					<?php
					foreach ($secoes as $secao):
					?>
					<div class="secao post bg">
						<div class="titulo-secao col col6"><h2><a href='<?php echo "/artigo.php?post=".$secao["titulo"]; ?>'><?php echo $secao["titulo"]; ?></a></h2></div>
						<div class="info-secao col col4">
							<?php 
							$sql = "SELECT * FROM users WHERE playerid = :usuarioid";
							$get = $banco->prepare($sql);
							$get->bindValue(":usuarioid", $secao["usuarioid"]);
							$get->execute();
							$usuario = $get->fetch(PDO::FETCH_ASSOC);
							?>
							<span><?php echo $usuario["Username"]; ?></span> -
							<span><?php echo $rank[$usuario["PrivLevel"]]; ?></span> -
							<span><?php $data = explode("-", $secao["data"]); echo "$data[2]/$data[1]/$data[0]"; ?></span>

							<?php if ($_SESSION["isAdmin"] == true):?>
							<a href="" title="Editar"><i class="fa fa-edit"></i></a>
							<a href='<?php echo "/sistema/CRUDArtigos.php?delete=true&id=" . $secao["id"]; ?>' title="Deletar"><i class="fa fa-window-close"></i></a>
							<?php endif; ?>
						</div>
					</div>
					<?php 
					endforeach;
					?>

					<?php 
					if ($_SESSION["isAdmin"] == true):
					?>
					<div class="secao post centT">
						<a class="botao azul" href='<?php echo "/novo_artigo.php?f=" . $_GET["f"] . "&a=" . $_GET["a"]; ?>' style="padding: 10px 50px;">NOVO</a>
					</div>

					<?php endif; ?>


				</div>
			</div>
		</div>

	</body>
</html>
<?php

$banco = null;

?>