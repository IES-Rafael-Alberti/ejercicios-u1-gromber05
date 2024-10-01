# Te pide el nombre de usuario y un número, lo que hace que lo repitas ese numero de veces
num = int(input('Introduce un número: '))
nombre = input('Introduce tu nombre de usuario: ')

# Y hace un bucle para imprimir el nombre ese número de veces
for i in range(0, num):
    print(nombre)