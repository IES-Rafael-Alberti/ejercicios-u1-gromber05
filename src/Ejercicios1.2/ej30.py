
num = int(input("Introduce un número: "))
incremento = int(input("Introduce el incremento: "))
num2 = int(input("Introduce el segundo número: "))

while incremento <= 0:
    print("Incremento no puede ser 0 o menor a cero")
    incremento = int(input("Introduce el incremento: "))

while num2 <= 0:
    print("El segundo numero no puede ser 0 o menor a cero")
    num2 = int(input("Introduce el segundo número: "))

serie = ""

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
print(f"SERIE => {serie}")