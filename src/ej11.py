# Pedimos el número
num = int(input('Introduzca un número: '))

# Detectamos si el número introducido no es negativo
if num > 0:
    # Si el número introducido no es negativo hacemos las operaciones y las imprimimos.
    num = num + 1
    num = num * num
    num = num / 2
    print('El resultado es: ' + str(num))
else:
    # Si el número es negativo, te salta el error.
    print('El número no puede ser negativo')