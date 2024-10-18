# Pedimos dos números de los tres
num1 = float(input('Introduzca el primer número: '))
num2 = float(input('Introduzca el segundo número: '))

# En esta operación sumamos el segundo número al primero y lo guardamos la suma en la primera
# variable para dejar la segunda vacía
num1 += num2  

# Volvemos a asignar un valor a num2
num2 = float(input('Introduzca el tercer número: '))
num1 += num2

# Imprimimos el resultado
print(f'El total de esos tres números es: {num1:.2f}')