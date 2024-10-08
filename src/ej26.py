# Te pide la lista de la compra y la separa
lista = input('Introduce tu lista de la compra separado por comas: ')
partes = lista.split(', ')

# Imprime cada producto en una linea nueva
for producto in partes:
    print(producto.lstrip().rstrip())