<?php
$salida= array(); //recogerá los datos que nos muestre el script de Python

    $tam="20";
    $ano = "1992";
	exec("python salt/nuevoAula.py '".$tam."' '".$ano."'", $salida);
	$miout = $salida[0];
	echo $miout;

    foreach ($salida as $val) {
    	echo "$val \n";
    }
?>