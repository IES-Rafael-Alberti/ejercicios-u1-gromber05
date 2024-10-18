import random

def numeroaleatorio(a, b):
    return random.randint(a, b+1)


def comprobarnumero(num: int, num2: int) -> int:
    if num == num2:
        print("Error los números introducidos son iguales")
    elif num2 < num:
        return num, num2
    else:
        return num2, num

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


def main():
    num, num2 = pedirNumero()

    c = numeroaleatorio(num, num2)
    print(f'El número aleatorio entre {num} y {num2} es {c}')



if __name__ == "__main__":
    main()