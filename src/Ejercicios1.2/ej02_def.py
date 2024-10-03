
def horario(horas, coste, total):
    return f"Importe total: {total} €"


def main():
    horas = int(input("¿Cuántas horas has realizado?: "))
    coste = int(input("Coste por hora del trabajo: "))
    total = horas * coste
    print(horario(horas, coste, total))


if __name__ == "__main__":
    main()