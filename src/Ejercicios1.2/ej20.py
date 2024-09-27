
numero = input('Introduce tú número de teléfono. TIene que tener el formato +34-número-extensión: ')

separar = numero.split('-')

numero_sin_prefijo_y_extension = separar[1]
print('El número de teléfono sin prefijo ni extensión es:', numero_sin_prefijo_y_extension)
