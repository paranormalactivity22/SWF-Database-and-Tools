<?php
session_start();

require_once "/sistema/ranking.php";

$ranking = new Ranking();

// Pegar Dados
if (isset($_POST["buscar"]) && !empty($_POST["nick"])):
	$nick = $_POST["nick"];
	if (!strpos($nick, "#")):
		$nick .= "#0000";
	endif;
	$rank[0] = $ranking->getRankingByName($nick);
else:
	$rank = $ranking->getRanking(3, "firstcount");
endif;

// Calcular Listas
if ($ranking->count):
	$tables = ceil($ranking->count/30);
else:
	$tables = 1;
endif;


// Definir pagina
if (isset($_POST["pagina"])):
	if (!empty($_POST["pagina"]) && is_int(intval($_POST["pagina"]))):
		$pagina = $_POST["pagina"];
	else:
		$pagina = 1;
	endif;
else:
	$pagina = 1;
endif;


// PAGINA
if ($pagina >= 2):
	$back = $pagina - 1;
else:
	$back = 1;
endif;

if ($pagina < $tables):
	$next = $pagina + 1;
else:
	$next = 1;
endif;


// Lista Ranking
$inicio = ($pagina-1) * 30;
$fim = ($pagina) * 30;


?>
<!DOCTYPE html>
<html>
	<head>
		<link rel="stylesheet" type="text/css" href="/css/main.css">
		<link rel="stylesheet" type="text/css" href="/css/forum.css">
		<link rel="stylesheet" type="text/css" href="/css/ranking.css">
		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
		<title>Ranking - MaiceMice</title>
		<link rel="icon" type="images/png" href="/img/favicon.png" />
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


		<div class="div-ranking">
			<div class="linha">
				<div class="ranking col col10 centC">
					<div class="ranking-infos coluna col6 voarD">
						<div class="col col4 voarD col10">
							<div class="menu-ranking voarD col10">
								<div class="voarD">
									<form action="" method="POST">
										<button class="botao-ranking azul" name="pagina" <?php echo 'value="'.$back.'"'; ?>>&laquo;</button>
										<span><?php echo "$pagina / $tables"; ?></span>
										<button class="botao-ranking azul" name="pagina" <?php echo 'value="'.$next.'"'; ?>>&raquo;</button>
									</form>
								</div>
								<div class="voarD" style="margin-right: 15px;">
									<form action="" method="POST" class="input-ranking">
										<input type="text" name="nick" placeholder="Nick#0000">
										<input class="botao-ranking azul" type="submit" name="buscar" value="Buscar" style="width: 57px;">
									</form>
								</div>
							</div>
						</div>
					</div>
					<div class="ranking-lista col col10 centC">
						<table class="centT col10">
							<div id="ranking">
								<tbody>
									<tr>
										<th>Lugar</th>
										<th>Nick</th>
										<th>Firsts</th>
										<th>Queijos</th>
										<th>Bootcamps</th>
										<th>Salvos</th>
										<th>Salvos Hard</th>
										<th>Salvos Divino</th>
									</tr>

									<?php

									$x = 0;
									foreach ($rank as $var):
										$x++;
										if (($x >= $inicio) && ($x <= $fim)):
									

									?>
									<tr>
										<td><?php echo $x; ?></td>
										<td><?php echo $var["username"]; ?></td>
										<td><?php echo $var["firstcount"]; ?></td>
										<td><?php echo $var["cheesecount"]; ?></td>
										<td><?php echo $var["bootcampcount"]; ?></td>
										<td><?php echo $var["shamansaves"]; ?></td>
										<td><?php echo $var["hardmodesaves"]; ?></td>
										<td><?php echo $var["divinemodesaves"]; ?></td>
									</tr>

									<?php
										else:
											continue;
										endif;
									endforeach;

									?>
								</tbody>
							</div>
						</table>
					</div>
				</div>
			</div>
		</div>


	</body>
</html>