
# Te pide el nombre de usuario
usuario = input('Introduzca su nombre de usuario: ')

# Primera frase y pone la primera en mayúscula
indice = 0
frase1 = usuario[:indice] + usuario[indice].upper() + usuario[indice + 1:]

# Segunda frase y lo pone todo en mayúsculas

frase2 = usuario.upper()

# Tercera frase y lo pone
# todo en minúsculas

frase3 = usuario.lower()

# Imprime las frases
print(frase1)
print(frase2)
print(frase3)