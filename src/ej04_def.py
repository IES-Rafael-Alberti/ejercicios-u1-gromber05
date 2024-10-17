# Establecemos la función cálculo
def calculo(celsius: float, fahrenheit: float) -> float:
    calcul = 5 / 9
    fahrenheit = (celsius * calcul) + 32
    return fahrenheit
    

# Establecemos la función principal que realizará el cálculo.
def main():
    celsius = float(input('Introduce los grados Celsius que quieras pasar a Fahrenheit: '))
    print(f"{celsius}º Celsius es igual a {fahrenheit:.2f}º Fahrenheit")

if __name__ == "__main__":
    main()