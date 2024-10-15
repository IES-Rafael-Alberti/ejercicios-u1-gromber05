
def fibonacci(n):
    serie = [0, 1]
    while True:
        siguiente_num = serie[-1] + serie[-2] 
        if siguiente_num > n:
            break
        serie.append(siguiente)
    return serie

def pedirNumero():
    num = int(input("Introduzca un número: "))
    while num == 0:
        return f"**ERROR** El número introducido no puede ser 0"
        num = int(input("Introduzca de nuevo un número: "))
    return num

def main():
    num = pedirNumero()
    calculo = fibonacci(num)
    print(f'La serie de Fibonacci para el número {num} es {calculo}')


if __name__ == "__main__":
    main()