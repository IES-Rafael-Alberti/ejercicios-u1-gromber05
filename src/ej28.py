
num1 = int(input("Ingrese un número: "))
num2 = int(input("Introduce otro número: "))

if num1 == num2:
    print("Ambos números no pueden ser iguales")
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
