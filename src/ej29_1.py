import random

"""
Para calcular un número aleatorio entre dos números, lo que debemos hacer es importar la librería 'random' y hacer una función
que calcule el número aleatorio con dicha libreria
"""

def numeroaleatorio(a, b):
    return random.randint(a, b+1)

"""
Luego comprobamos si son iguales o si no, y si no son iguales, cual es el número mayor.
"""

def comprobarnumero(num: int, num2: int) -> int:
    if num == num2:
        print("Error los números introducidos son iguales")
    elif num2 < num:
        return num, num2
    else:
        return num2, num
"""
En esta función lo que hacemos es que nos pida un número y nos identifique si es 0, si el caso es verdadero
Lo que nos hace la función es que nos devuelve una cadena de texto.
"""
def pedirNumero(num: int, num2: int) -> int:
    num = input("Introduce el primer número: ")
    num2 = input("Introduce el segundo número: ")
    while num == 0:
        return f"**ERROR** El número introducido no puede ser 0"
        num = input("Introduzca de nuevo un número: ")
    while num2 == 0:
        return f"**ERROR** El número introducido no puede ser 0"
        num2 = input("Introduzca de nuevo un número: ")
    return num, num2


"""
Y por último, en la función main imprimimos el resultado
"""

def main():
    num, num2 = pedirNumero()

    c = numeroaleatorio(num, num2)
    print(f'El número aleatorio entre {num} y {num2} es {c}')



if __name__ == "__main__":
    main()