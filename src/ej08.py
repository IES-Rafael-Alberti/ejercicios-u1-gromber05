# Pedimos dos números de los tres
num1 = int(input('Introduzca el primer número: '))
num2 = int(input('Introduzca el segundo número: '))

# En esta operación sumamos el segundo número al primero y lo guardamos la suma en la primera
# variable para dejar la segunda vacía
num1 += num2  

# Volvemos a asignar un valor a num2
num2 = int(input('Introduzca el tercer número: '))

# Imprimimos el resultado
print('El total de esos tres números es: ' + str(num1 + num2) )