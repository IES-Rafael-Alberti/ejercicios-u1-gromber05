
# Aqui te pide la edad y el nombre del sujeto
edad = int(input("Ingrese su edad: "))
nombre = input("Ingrese su nombre: ")

# La primera cadena de if y else lo que hace es detectar si el nombre está vacío o no
# Luego las segundas cadenas, lo que hace es calcular el rango de edad e imprimir el resultado
if nombre == "":
    if edad > 0 or edad < 125:
        numeros = range(edad, 125)
        cantidad = len(numeros)
        print(f"Te llamas Desconocido y tienes {edad} años, te quedan aún {cantidad} por cumplir")
    else:
        print("La edad introducida no puede ser menor a 0 o mayor a 125")
else:
    if edad > 0 or edad < 125:
        numeros = range(edad, 125)
        cantidad = len(numeros)
        print(f"Te llamas {nombre} y tienes {edad} años, te quedan aún {cantidad} por cumplir")
    else:
        print("La edad introducida no puede ser menor a 0 o mayor a 125")