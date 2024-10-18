
def fahrenheit():
    celsius = float(input('Introduce los grados Celsius que quieras pasar a Fahrenheit: '))
    calcul = 9 / 5
    fahrenheit = (celsius * calcul) + 32
    print(f"{celsius}º C ({fahrenheit:.2f}º F)")
    


def main():
    fahrenheit()

if __name__ == "__main__":
    main()