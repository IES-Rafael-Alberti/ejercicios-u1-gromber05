
frase = input('Introduce una frase: ')
letra = input('Introduce una vocal: ')


if letra in ('a', 'e', 'i', 'o', 'u'):
    frase1 = frase.replace(letra, letra.upper())
    print(frase1)
else:
    print('La letra introducida no puede ser una distinta de una vocal')
