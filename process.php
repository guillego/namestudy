<html>
<head>
<title>Trabajo SALT</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
</head>
<body>
<?php
	$tam= $_POST['tam'];
	$ano = $_POST['ano'];


		echo "Muestra de una clase de ". $tam . " personas nacidas en el año " . $ano . ".<br />";

	$salida= array(); //recogerá los datos que nos muestre el script de Python
	$texto="Hola Mundo";

	    exec("python salt/nuevoAula.py '".$tam."' '".$ano."'",$salida);
	    $sal = array_slice($salida, 1);
	    $miout =$salida[0];
?>
<img src=<?php echo $miout;?> alt="Barras" >
<?php
foreach ($sal as $val) {
	echo $val ."<br />";
}
?>
</body>
</html>