<?php
session_start();

require_once("/sistema/config.php");
require_once("/sistema/conexao.php");
require_once("/sistema/login.php");

$conexao = new Conexao();
$banco = $conexao->getCon();

$sql = "SELECT * FROM forum";
$get = $banco->prepare($sql);
$get->execute();

$forums = $get->fetchAll(PDO::FETCH_ASSOC);

?>
<!DOCTYPE html>
<html>
	<head>
		<link rel="stylesheet" type="text/css" href="/css/main.css">
		<link rel="stylesheet" type="text/css" href="/css/forum.css">
		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
		<title>Forum - MaiceMice</title>
		<link rel="icon" type="images/png" href="/img/favicon.png">
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


		<div class="display-forum">
			<div class="linha">
				<div class="forum-tabelas col col10">
					<?php
					foreach ($forums as $forum):
					?>
					<div id='<?php echo "forum-".$forum["titulo"]; ?>' class="forum-tabela">
						<div class="header-tabela">
							<a href='<?php echo "#forum-".$forum["titulo"]; ?>'>
								<div class="col col10">
									<div class="col voarE">
										<h2 class="titulo-section"><?php echo $forum["icone"] . " " . $forum["titulo"]; ?></h2>
									</div>
									<div class="col voarD">
								<?php if ($_SESSION["isAdmin"] == true): ?>
									<div class="col col2 voarE" style="display: contents;font-size: 20px;">
										<a href="" style="margin-left: 3px;" title="Editar"><i class="fa fa-edit"></i></a>
										<a href='<?php echo "/sistema/CRUDForum.php?delete=true&id=" . $forum["ID"]; ?>' style="margin-left: 3px;" title="Deletar"><i class="fa fa-window-close"></i></a>
									</div>
								<?php endif; ?>
										<span>
											+
										</span>
									</div>
								</div>
							</a>
						</div>

						<div class="bodys-forum">
							<?php
							$sql = "SELECT * FROM artigo WHERE forum = :forumid";
							$get = $banco->prepare($sql);
							$get->bindValue(":forumid", $forum["ID"]);
							$get->execute();
							$artigos = $get->fetchAll(PDO::FETCH_ASSOC);
							foreach ($artigos as $artigo):
							?>
							<div class="body-forum col">
								<div class="forum-body-header">
									<div class="col col3">
										<a href='<?php echo "/secao.php?f=".$artigo["id"]."&a=".$forum["ID"]; ?>'><?php echo $artigo["icone"]; ?> <?php echo $artigo["titulo"]; ?></a>
									</div>
									<div class="col col4">
										<a href='<?php echo "/artigo.php?post=".$artigo["ultimo"] ?>'><?php echo $artigo["ultimo"]; ?></a> 
									</div>
									<?php

									if ($_SESSION["isAdmin"] == true):
									?>
									<div class="col col2 voarD" style="text-align: right;">
										<a href="" title="Editar"><i class="fa fa-edit"></i></a>
										<a href='<?php echo "/sistema/CRUDArtigo.php?delete=true&id=".$artigo["id"]; ?>' title="Deletar"><i class="fa fa-window-close"></i></a>
									</div>
									<?php
									endif;
									?>
								</div>
							</div>
							<?php
							endforeach;
							?>

							<?php

							if ($_SESSION["isAdmin"] == true):

							?>
							<div class="body-forum col">
								<div class="forum-body-header">
									<div class="col col10">
										<form action="/sistema/CRUDArtigo.php" method="POST">
											<input class="inputinv" type="text" name="icone" placeholder="icone">
											<input class="inputinv" type="text" name="titulo" placeholder="Nome do Artigo">
											<input type="hidden" name="id" value='<?php echo $forum["ID"]; ?>'>
											<input class="botao azul" name="criar" type="submit" value="criar" style="padding: 4px 11px;">
										</form>
									</div>
								</div>
							</div>
							<?php
							endif;
							?>
						</div>
					</div>
					<?php
					endforeach;
					?>
					<?php if ($_SESSION["isAdmin"] == true): ?>
					<div class="forum-tabela">
						<div class="header-tabela">
							<div class="col col10">
								<form action="/sistema/CRUDForum.php" method="POST" style="margin: 5px;">
									<input class="inputinv" type="text" name="icone" placeholder="icone">
									<input class="inputinv" style="font-size: 20px;font-weight: bold;" type="text" name="titulo" placeholder="Nome do Forum">
									<input type="hidden" name="id" value='<?php echo $forum["ID"]; ?>'>
									<input class="botao azul" name="criar" type="submit" value="criar" style="padding: 4px 11px;">
								</form>
							</div>
						</div>
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