
precio = float(input('¿Cuánto te ha costado?: '))
precio1 = round(precio, 2)
precio2 = str(precio1)

precioc = precio1 * 100
precioct = int(precioc)
preciocts = str(precioct)

print(f'El precio del producto en euros ha sido de: {precio2}€ y el precio en céntimos ha sido de {preciocts} céntimos')