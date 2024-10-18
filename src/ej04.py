# Preguntamos por los grados Celsius que se quieran convertir y los pasamos a string
celsius = float(input('Introduce los grados Celsius que quieras pasar a Fahrenheit: '))

# Hacemos el calculo necesario para pasar a fahrenheit
calculo = 5 / 9


# Pasamos los grados a farenheit y pasamos el valor de la variable de integer a string
fahrenheit = celsius * calculo
fahrenheit = fahrenheit + 32

# Imprimimos por pantalla esa variable
print(f'{celsius:.2f}º Celsius es igual a {fahrenheit:.2f}º en Fahrenheit')