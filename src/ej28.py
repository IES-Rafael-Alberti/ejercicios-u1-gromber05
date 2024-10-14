
# Primero pedimos los dos números
num1 = int(input("Ingrese un número: "))
num2 = int(input("Introduce otro número: "))

# Aquí detecta que los números no pueden ser iguales, por lo que salta un error
if num1 == num2:
    print("Ambos números no pueden ser iguales")
# Aquí lo que hace es que si detecta que el segundo numero introducido es mayor al primero, los intercambia y cuenta cuantos numeros hay entre esos dos números
elif num1 > num2:
    temp = num1
    num1 = num2
    num2 = temp
    numeros = range(num1 ,num2)
    cantidad = len(numeros)
    print(f"Entre el número {num1} y el número {num2}, hay {cantidad} números")
else:
    numeros = range(num1 ,num2)
    cantidad = len(numeros)
    print(f"Entre el número {num1} y el número {num2}, hay {cantidad} números")
