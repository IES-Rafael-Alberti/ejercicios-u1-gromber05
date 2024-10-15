
def divisores(n):
    a = []
    for i in range(1, n + 1):
        if n % i == 0:
            a.append(i)
    return a

def pedirNumero():
    num = int(input("Introduzca un número: "))
    while num == 0:
        return f"**ERROR** El número introducido no puede ser 0"
        num = int(input("Introduzca de nuevo un número: "))
    return num

def main():
    num = pedirNumero()
    a = divisores(num)
    print(f'Los divisores de {num} son {a}')

if __name__ == "__main__":
    main()