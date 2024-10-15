# Establecemos la funcion del horario
def horario(horas, coste):
    total = horas * coste
    return total

# Establecemos la funcion main que pedira las horas y el coste, y las calculará.
def main():
    horas = int(input("¿Cuántas horas has realizado?: "))
    coste = int(input("Coste por hora del trabajo: "))
    total = horario(horas, coste)
    print(f"Importe total: {total} €")


if __name__ == "__main__":
    main()