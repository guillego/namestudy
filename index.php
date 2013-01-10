<html>
<head>
<title>Trabajo SALT</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
</head>
    <body>
        <h2>SALT:Estudio de los nombres de la población norteamericana</h2>
            <h3>Simulador de un conjunto de población</h3>
                <h4>Dado un año de nacimiento y un número de personas, se simula la distribución de nombres entre las distintas personas</h4>
                    <form action="process.php" method="post">
                        <select name="ano">
                            <?php
                            foreach (range(1900, 2011) as $number) {
                            echo "<option>$number</option>";
                            }
                            ?>
                        </select>
                        Tamaño de la clase <input name="tam" type="text" /> </br>
                        Género: </br>
                        Masculino <input type="Radio" name="gender" value="male"> </br>
                        Femenino <input type="Radio" name="gender" value="female">
                        </br>
                        <input type="submit" />
                    </form>
            <h3>Ejemplo de distribución</h3>
                <h4>Muestra como se han distribuido los nombres dado un conjunto de 20 personas, a lo largo de los últimos 111 años</h4>
                    <form action="progresion.php" method="post">
                       Ver: <input type="submit" />
                    </form>
    </body>
</html>
