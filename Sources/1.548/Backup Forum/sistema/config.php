<?php

require_once "/sistema/conexao.php";
require_once "/sistema/login.php";

$rank = array(
	12 => "Fundador",
	11 => "Administrador",
	10 => "Coordenador",
	9 => "Super Moderador",
	8 => "Moderador",
	7 => "MapCrew",
	6 => "Ajudante",
	5 => "Trial Mod",
	4 => "Trial Mpc",
	3 => "Vip Master",
	2 => "Vip",
	1 => "Player",
	0 => "bloqueado"
);


$_SESSION['isAdmin'] = false;

if (isset($_SESSION["logado"])):
	$login = new Login();
	$dados = $login->getInfosByNick($_SESSION["nick"]);
	if ($dados["PrivLevel"] >= 12):
		$isAdm = true;
		$_SESSION['isAdmin'] = true;
	else:
		$isAdm = false;
		$_SESSION['isAdmin'] = false;
	endif;
endif;

?>