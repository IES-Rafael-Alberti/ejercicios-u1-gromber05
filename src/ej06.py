# Pedimos el precio del producto con un 10% de IVA
importe = float(input('Dime cuánto te ha costado el producto (10% de IVA): '))

# Calculamos ese IVA
iva = importe * 0.1

# Calculamos el precio del importe sin IVA
precio_inicial = importe - iva

# Imprimimos los resultados
print(f'El IVA ha sido un total de: {iva:.2f}')
print(f'El precio sin IVA era un total de: {precio_inicial:.2f}')