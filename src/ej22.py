# Te pide una frase y una vocal
frase = input('Introduce una frase: ')
letra = input('Introduce una vocal: ')

# Si la letra introducida es una vocal, pone esa misma letra en mayuscula
if letra in ('a', 'e', 'i', 'o', 'u'):
    frase1 = frase.replace(letra, letra.upper())
    print(frase1)
else:
    print('La letra introducida no puede ser una distinta de una vocal')
