# Te pide un email
email = input('Introduce tú email: ')

# Lo separa por el arroba
separar = email.split('@')

# Y lo imprime con el nuevo sufijo de email
email1 = separar[0]
print('Tu nuevo correo es: ' + email1 + '@ceu.es')