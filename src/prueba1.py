
def comparacion(a, b):
    while a == b:
        print("Error, los número no pueden ser iguales")
    else:
        if a > b:
            return f"{a} > {b}"
        else:
            return f"{b} > {a}"

def num():
    num1 = int(input("Introduzca un número: "))
    num2 = int(input('Introduzca otro número: '))
    resultado = comparacion(num1, num2)
    return resultado


def main():
    comparacion = num()
    print(f'{comparacion}')

if __name__ == "__main__":
    main()