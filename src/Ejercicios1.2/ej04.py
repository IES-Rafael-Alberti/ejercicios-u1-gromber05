# Preguntamos por los grados Celsius que se quieran convertir y los pasamos a string
celsius = int(input('Introduce los grados Celsius que quieras pasar a Fahrenheit: '))

# Hacemos el calculo necesario para pasar a fahrenheit
calculo = 5 / 9

# Pasamos los grados a farenheit y pasamos el valor de la variable de integer a string
fahrenheit = str(celsius * calculo)

# Imprimimos por pantalla esa variable
print(celsiusstr + ' grados es igual a ' + fahrenheit + ' en Fahrenheit')