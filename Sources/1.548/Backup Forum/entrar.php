<?php

require_once "/sistema/login.php";
session_start();

if (isset($_SESSION["logado"])) {
	header("Location: /index.php");
}

$erro = "";
if (isset($_POST["nick"]) && isset($_POST["senha"])):
	if (!empty($_POST["nick"]) && !empty($_POST["senha"])):
		$nick = $_POST["nick"];
		$senha = $_POST["senha"];

		if (!stristr($nick, '#')){
			$nick = $nick."#0000";
		}

		$login = new Login();
		$dados = $login->getPassword($nick);

		if ($dados !== false):
			if ($dados["password"] == $senha):
				$_SESSION['logado'] = true;
				$_SESSION['nick'] = $dados["username"];
				header("Location: ./index.php");
			else:
				$erro = "Senha Inválida";
			endif;
		else:
			$erro = "Usuário não foi encontrado";
		endif;
	else:
		$erro = "Preencha os campos.";
	endif;
endif;
?>
<!DOCTYPE html>
<html>
	<head>
		<script src="/css/script.js"></script>
		<link rel="stylesheet" type="text/css" href="/css/main.css">
		<link rel="stylesheet" type="text/css" href="/css/forum.css">
		<link rel="stylesheet" type="text/css" href="/css/forum-login.css">
		<title>Entrar - MaiceMice</title>
		<link rel="icon" type="images/png" href="/img/favicon.png" />
		<meta charset="utf-8">
		<script>
			function encode(){
				var pass = document.getElementById("pass");
				var passcript = document.getElementById("passcript");
				var newpass = crypte(pass.value);
				passcript.value = newpass;

				var pass = document.getElementById("go");
				pass.click();
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
								<li><a href="/index.php">Forum</a></li>
							</ul>
						</nav>
					</div>
				</div>
			</header>
		</div>


		<div class="login">
			<div class="linha">
				<div class="login-box col col3 centC bg centT bd">
					<h2>Entrar</h2>
					<form class="form-forum" action="./entrar.php" method="POST" autocomplete="off">
						
						<input type="text" name="nick" placeholder="Nick" required="required">
						
						
						<input id="passcript" type="hidden" name="senha" required="required">
						
						
						
						<input style="display: none;" id="go" type="submit">

					</form>

					<input id="pass" class="formedit" type="password" name="senhauncript" placeholder="Senha" required="required">
					<input class="botao azul formedit" id="gocript" type="button" value="Entrar" onclick="encode()">

					<span><?php echo $erro; ?></span>
				</div>
			</div>

			<script>
				var input = document.getElementById("pass");
				input.addEventListener("keyup", function(event) {
				  if (event.keyCode === 13) {
				   event.preventDefault();
				   document.getElementById("gocript").click();
				  }
				});
			</script>
		</div>


	</body>
</html>