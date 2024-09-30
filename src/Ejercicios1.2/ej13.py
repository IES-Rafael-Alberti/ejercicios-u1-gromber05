# Pedimos los dos números necesarios
num1 = int(input('Introduzca el primer número: '))
num2 = int(input('Introduzca el segundo número: '))

# Realizamos las operaciones necesarias
div = str(num1 / num2)
div2 = str(num1 % num2)

# Imprimimos los resultados
print('La división entre ' + str(num1) + ' y ' + str(num2) + ' da de cociente '+ div + ' y da de resto ' + div2)