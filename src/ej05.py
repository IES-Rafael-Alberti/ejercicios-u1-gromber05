# Preguntamos por el precio sin IVA
precio = float(input('Dime el precio sin IVA del producto:' ))

# Preguntamos por el porcentaje de IVA que ha pagado
iva = float(input('Dime el porcentaje de IVA que has pagado (21% : 0.21)' ))

# Miramos si el IVA es válido.
if iva < 1 or iva > 0:
    # Si el iva introducido es válido, calculamos el precio con iva y lo imprimimos
    iva_calculado = precio * iva
    precio_final = str(precio + iva_calculado)
    precio_final = float(precio_final)
    print(f'El precio final es de: {precio_final:.2f}')

else:
    # Si el iva introducido no es válido, se imprimirá este resultado
    print('El IVA introducido no puede ser mayor a 1.00 o menor a 0.00')