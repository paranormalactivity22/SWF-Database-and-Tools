<?php

session_start();
session_unset();
session_destroy();

if (!isset($_SESSION["logado"])) {
	header("Location: /index.php");
}




?>