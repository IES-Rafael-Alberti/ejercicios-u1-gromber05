
importe = float(input('Dime cuánto te ha costado el producto (10% de IVA): '))

iva = importe * 0.1

importestr = importe

precio_inicial = importestr - iva

print('El IVA ha sido un total de: ' + str(iva))
print('El precio sin IVA era un total de: ' + str(precio_inicial))