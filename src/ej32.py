"""
Para calcular la serie de Fibonacci, agregaremos una función que haga una serie, y le vaya añandiendo cada número que cumpla con la regla
de Fibonacci

Args:
    n (int): El número al que queremos calcular la serie de Fibonacci

Returns:
    str: La serie del número de Fibonacci

"""

def fibonacci(n: int) -> str:
    serie = [0, 1]
    while True:
        siguiente_num = serie[-1] + serie[-2] 
        if siguiente_num > n:
            break
        serie.append(siguiente_num)
    return serie

"""
Luego añadimos la función para pedirle un número y comprobar que el número introducido no sea cero

Args:
    

Returns:
    int: El número que se ha pedido

"""

def pedirNumero() -> int:
    num = int(input("Introduzca un número: "))
    while num == 0:
        return f"**ERROR** El número introducido no puede ser 0"
        num = input("Introduzca de nuevo un número: ")
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