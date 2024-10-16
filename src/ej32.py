"""
Para calcular la serie de Fibonacci, agregaremos una función que haga una serie, y le vaya añandiendo cada número que cumpla con la regla
de Fibonacci
"""

def fibonacci(n):
    serie = [0, 1]
    while True:
        siguiente_num = serie[-1] + serie[-2] 
        if siguiente_num > n:
            break
        serie.append(siguiente)
    return serie

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
    calculo = fibonacci(num)
    print(f'La serie de Fibonacci para el número {num} es {calculo}')


if __name__ == "__main__":
    main()