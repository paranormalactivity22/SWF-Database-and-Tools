<?php
session_start();

if (!isset($_SESSION["logado"])) {
	header("Location: /entrar.php");
}

require_once "/sistema/login.php";

$login = new Login();
$nick = $_SESSION["nick"];
$email = $login->getEmail($nick);

$status = "";
if (isset($_POST["oldpass"]) && isset($_POST["newpass"])):
	if (!empty($_POST["oldpass"]) && !empty($_POST["newpass"])):
		$change = $login->changePassword($_SESSION["nick"], $_POST["oldpass"], $_POST["newpass"]);
		if ($change == true):
			$status = "<br>Senha alterada com sucesso";
		else:
			$status = "<br>Não foi possivel alterar sua senha, tente novamente.";
		endif;
	endif;
endif;

?>
<!DOCTYPE html>
<html>
	<head>
		<script src="/css/script.js"></script>
		<link rel="stylesheet" type="text/css" href="/css/main.css">
		<link rel="stylesheet" type="text/css" href="/css/forum.css">
		<title>Configurações <?php echo"$nick"; ?></title>
		<link rel="icon" type="images/png" href="/img/favicon.png" />
		<meta charset="utf-8">
		<script>
			function encode(){
				var oldpass = document.getElementById("oldpass");
				var newpass = document.getElementById("newpass");

				if (newpass.value.length >= 8) {
					oldpass.value = crypte(oldpass.value);
					newpass.value = crypte(newpass.value);
				} else {
					alert("Sua Senha deve conter 8 ou mais caracteres.");
				}

				//var pass = document.getElementById("mudar");
				//pass.click();
			}
		</script>
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
								<li><a href="/index.php">Inicío</a></li>
								<li><a href="index.php">Forum</a></li>
								<li><a href="sair.php">Sair</a></li>
							</ul>
						</nav>
					</div>
				</div>
			</header>
		</div>


		<div class="configs">
			<div class="linha">
				<div class="col col10 bg margin bd">
					<div class="menu-header">
						<ul class="menu-forum menuH spaddin smargin">
							<li><a href="#config-conta">Conta</a></li>
							<li><a href="#mudar-senha">Mudar Senha</a></li>
							<li><a href="#comprar-vip">Area de Compras</a></li>
						</ul>
					</div>
					<div class="hr smargin"></div>
					<div id="config-conta" class="menu-conteudo">
						<span>Nick: <?php echo $_SESSION["nick"]; ?></span>
						<span>Email: <?php echo $email; ?></span>
					</div>
					<div >
					<div id="mudar-senha" class="menu-conteudo">
						<form class="fbtao" action="./configurar.php#mudar-senha" method="POST">
							<span>Mude de senha, lembre-se de nunca compartilhar-la com ninguém.</span>
							<input id="oldpass" type="password" name="oldpass" placeholder="Senha Antiga">
							<input id="newpass" type="password" name="newpass" placeholder="Senha Nova">
							<button class="botao azul" onclick="encode()">Mudar</button>
						</form>
						<span id="stts"><?php echo $status; ?></span>
					</div>
					<div id="comprar-vip" class="menu-conteudo">
		
					<div class="b">
					<h4>&#11088; Loja MaiceMice &#11088;</h4>
						<p>
							Ja pensou em ter privilegios especiais no MaiceMice? 
							então chegou sua hora, nós diretores do MaiceMice tiramos um dia analisando preços e decidimos trazer alguns pacotes para você aproveitar muito e se divertir!
						</p>
						</div>
						<br>
						<span class="b">Vip Simples</span>
						<span>Preço: 12,00 $ (Reais)</span>
						<a href="https://discord.gg/mWxrMGY" target="_blank"><button class="botao verde">comprar vip</button></a>
						<br><br>
						<span  class="b">Vip Master</span>
						<span>Preço: 16,00 $ (Reais)</span>
						<a href="https://discord.gg/mWxrMGY" target="_blank"t><button class="botao verde">comprar vip</button></a>
						<br><br>
						<span class="b">Mudar Nick</span>
						<span>Preço: 10,00 $ (Reais)</span>
						<a href="https://discord.gg/mWxrMGY" target="_blank"><button class="botao verde">Mudar Nick</button></a>
						<br><br>
						<span class="b">Comprar + no Nick</span>
						<span>Preço: 17,00 $ (Reais)</span>
						<a href="https://discord.gg/nHdsczn" target="_blank"><button class="botao verde">Mudar Nick</button></a>
					</div>
				</div>
			</div>
		</div>


	</body>
</html>