# Preguntamos cuántas horas hemos realizado
# horas = int(input("¿Cuántas horas has realizado?: \n"))
# Preguntamos cuánto cuesta cada hora de trabajo
# coste = int(input("Coste por hora del trabajo: \n"))
# Calculamos el coste final de todas las horas
# total = str(horas * coste)
# Imprimimos ese cálculo
# print("Importe total: " + total) 

def horario(horas, coste, total):
    return f"Importe total: {total} €"


def main():
    horas = int(input("¿Cuántas horas has realizado?: "))
    coste = int(input("Coste por hora del trabajo: "))
    total = horas * coste
    print(horario(horas, coste, total))


if __name__ == "__main__":
    main()