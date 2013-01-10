<html>
<head>
<title>Trabajo SALT</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
</head>
<body>
<?php
	$male_status = 'unchecked';
	$female_status = 'unchecked';
	$genero = 0;
	$personas = 'hombres';
	$let='o';
	
	$tam= $_POST['tam'];
	$ano = $_POST['ano'];
	$selected_radio = $_POST['gender'];

	if ($selected_radio == 'male') {
		$genero = 0;
		$personas = 'hombres';
		$let='o';
		$male_status = 'checked';
	}

	else if ($selected_radio == 'female') {
		$genero = 1;
		$personas = 'mujeres';
		$let='a';
		$female_status = 'checked';
	}	
	
		echo "Muestra de una clase de ". $tam . " ".$personas." nacid".$let."s en el año " . $ano . ".<br />";

	$salida= array(); //recogerá los datos que nos muestre el script de Python
	$texto="Hola Mundo";

	    exec("python salt/nuevoAula.py '".$tam."' '".$ano."' '".$genero."' ",$salida);
	    $sal = array_slice($salida, 3);
	    $miout0 =$salida[0];
	    $miout1 =$salida[1];
	    $miout2 =$salida[2];
?>
<img src=<?php echo $miout0;?> alt="Barras" > <img src=<?php echo $miout1;?> alt="Barras" > <img src=<?php echo $miout2;?> alt="Barras" ><br/>
<?php
foreach ($sal as $val) {
	echo $val ."<br />";
}
?>
</body>
</html>