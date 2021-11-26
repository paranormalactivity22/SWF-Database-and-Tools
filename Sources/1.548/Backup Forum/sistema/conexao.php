<?php

class Conexao {

	private $con;

	public function __construct() {
		try {
			$this->con = new PDO("mysql:host=localhost:3306;dbname=maicemice;charset=utf8", "root", "88096506cidartha");
			$this->con->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
		} catch (PDOException $error) {
			echo "Erro ao se conectar com o banco de dados.";
		} catch (Exception $error) {
			echo "Erro: $erro";
		}
	}

	public function getCon() {
		return $this->con;
	}

	public function closeCon() {
		$this->con = Null;
		return $this->con;
	}

}

?>