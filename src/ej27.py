# Te pide el nombre, el precio y las unidades
nombre = input('Dime el nombre del producto: ')
precio = float(input('Dime el precio: '))
unidades = int(input('Dime unidades: '))

# Te calcula el precio por unidad
preciofinal = precio/unidades


print(f'{nombre} {preciofinal:09.2f} {unidades:03d} {precio:011.2f}')