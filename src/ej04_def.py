# Establecemos la función cálculo
def calculo(celsius, fahrenheit):
    return f"{celsius} grados Celsius es igual a {fahrenheit:.2f} grados Fahrenheit"

# Establecemos la función principal que realizará el cálculo.
def main():
    calcul = 5 / 9
    celsius = float(input('Introduce los grados Celsius que quieras pasar a Fahrenheit: '))
    fahrenheit = (celsius * calcul) + 32
    print(calculo(celsius, fahrenheit))

if __name__ == "__main__":
    main()