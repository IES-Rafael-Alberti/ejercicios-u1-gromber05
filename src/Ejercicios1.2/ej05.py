
precio = float(input('Dime el precio sin IVA del producto:' ))

iva = float(input('Dime el porcentaje de IVA que has pagado (21% : 0.21)' ))

if iva < 1 or iva > 0:
    iva_calculado = precio * iva
    precio_final = str(precio + iva_calculado)
    print('El precio final es de: ' + precio_final)

else:
    print('El IVA introducido no puede ser mayor a 1.00 o menor a 0.00')