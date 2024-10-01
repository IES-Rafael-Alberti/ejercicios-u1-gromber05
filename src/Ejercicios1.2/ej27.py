# Te pide el nombre, el precio y las unidades
nombre = input('Dime el nombre del producto: ')
precio = float(input('Dime el precio: '))
unidades = int(input('Dime unidades: '))

# Te calcula el precio por unidad
preciofinal = precio/unidades

# Y te imprime el resultado
print(f'{nombre} cuesta {preciofinal:.2f}, hay una cantidad de {unidades} y todo cuesta {precio}')