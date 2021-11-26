<?php
session_start();

require_once "/sistema/config.php";
require_once "/sistema/conexao.php";

$conexao = new Conexao();
$banco = $conexao->getCon();


if($_SESSION["isAdmin"] != true){
	header("Location: /index.php");
}

if (isset($_GET["f"]) && isset($_GET["a"]) && !empty($_GET["a"]) && !empty($_GET["f"])){
	$forum = $_GET["f"];
	$artigo = $_GET["a"];
} else{
	header("Location: /index.php");
}


?>
<!DOCTYPE html>
<html>
	<head>
		<link rel="stylesheet" type="text/css" href="/css/main.css">
		<link rel="stylesheet" type="text/css" href="/css/forum.css">
		<link rel="stylesheet" type="text/css" href="/css/artigo.css">
		<link rel="stylesheet" type="text/css" href="/css/novo_artigo.css">
		<meta charset="utf-8">
		<title>Novo Artigo</title>
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
				
				<form action="/sistema/CRUDArtigos.php" method="POST">
					<div class="artigotitulo col col10 bg margin bd">
						<input type="text" name="titulo" placeholder="Titulo">
					</div>
					<div class="artigo col col10 bg margin bd">
						<div class="artigo-conteudo centT conteudo col col10">
							<textarea name="conteudo"><p>Opa</p></textarea>
							<input type="hidden" name="forum" value='<?php echo $forum; ?>'>
							<input type="hidden" name="artigo" value='<?php echo $artigo; ?>'>
							<input class="botao azul" type="submit" name="criar" value="Postar">
						</div>
					</div>
				</form>
			</div>
		</div>


	</body>
</html>
