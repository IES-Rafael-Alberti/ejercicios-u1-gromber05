"""
Para calcular los divisores de un número, crearemos una función llamda divisores en la que calcularemos los divisores del
valor que se introduzca en dicha función.
"""

def divisores(n):
    a = []
    for i in range(1, n + 1):
        if n % i == 0:
            a.append(i)
    return a

"""
Luego añadimos la función para pedirle un número y comprobar que el número introducido no sea cero
"""

def pedirNumero():
    num = int(input("Introduzca un número: "))
    while num == 0:
        return f"**ERROR** El número introducido no puede ser 0"
        num = int(input("Introduzca de nuevo un número: "))
    return num

"""
Y por último, en la función main imprimimos el resultado
"""

def main():
    num = pedirNumero()
    a = divisores(num)
    print(f'Los divisores de {num} son {a}')

if __name__ == "__main__":
    main()