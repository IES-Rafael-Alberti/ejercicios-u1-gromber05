# Primero pedimos los los dos numeros en los que se recogerá la serie y el incremento
num = int(input("Introduce un número: "))
incremento = int(input("Introduce el incremento: "))
num2 = int(input("Introduce el segundo número: "))

# Si el incremento es menor o igual a cero, vuelve a pedir el incremento
while incremento <= 0:
    print("Incremento no puede ser 0 o menor a cero")
    incremento = int(input("Introduce el incremento: "))

# Si el número 2 es menor o igual a cero, vuelve a pedir el número
while num2 <= 0:
    print("El segundo numero no puede ser 0 o menor a cero")
    num2 = int(input("Introduce el segundo número: "))

# Establece la serie
serie = ""

# Aquí escribe los carácteres necesarios para que funcione la serie
for i in range(num2):
    cont = num + (i * incremento)  
    if i == 0:
        serie += str(cont) + '-'
    elif i == num2 - 1:
        serie += '-' + str(cont)
    elif i == 1:
        serie += str(cont)
    else:
        serie += '..' + str(cont)
# Aquí se imprime la serie
print(f"SERIE => {serie}")