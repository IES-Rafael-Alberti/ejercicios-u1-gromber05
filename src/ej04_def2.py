
def grados_celsius(farenheit: float) -> float:
    calculo1 = farenheit * (9 / 5)
    calculo2 = calculo1 + 32
    return calculo2

def main():
    celsius = float(input("Introduce los grados que quieras convertir a fahrenheit: "))
    celsius = round(celsius, 2)
    farenheit = grados_celsius(farenheit=celsius)
    print(f"Los grados introducidos en Celsius son {farenheit}º Fahrenheit")

if __name__ == "__main__":
    main()