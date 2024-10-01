# Pedimos el número
num = int(input('Introduzca un número: '))

# Detectamos si el número introducido no es negativo
if num > 0:
    # Si el número introducido no es negativo hacemos las operaciones y las imprimimos.
    o1 = num + 1
    o2 = num * o1
    o3 = o2 / 2
    print('El resultado es: ' + str(o3))
else:
    # Si el número es negativo, te salta el error.
    print('El número no puede ser negativo')