# Te pide el número de teléfono con prefijo y el sufijo
numero = input('Introduce tú número de teléfono. TIene que tener el formato +34-número-extensión: ')

# Lo separa por una extensión -
separar = numero.split('-')

# Separa el número y lo imprime en pantalla
numero_sin_prefijo_y_extension = separar[1]
print(f'El número de teléfono sin prefijo ni extensión es: {numero_sin_prefijo_y_extension}')
