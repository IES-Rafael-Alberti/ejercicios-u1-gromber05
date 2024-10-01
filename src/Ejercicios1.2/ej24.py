# Te pregunta por el precio y lo redondea
precio = float(input('¿Cuánto te ha costado?: '))
precio1 = round(precio, 2)
precio2 = str(precio1)

# Hace las operaciones necesarias para pasarlo a céntimos
precioc = precio1 * 100
preciocts = str(int(precioc))

# Imprime el resultado
print(f'El precio del producto en euros ha sido de: {precio2}€ y el precio en céntimos ha sido de {preciocts} céntimos')