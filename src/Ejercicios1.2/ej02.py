# Preguntamos cuántas horas hemos realizado
horas = int(input("¿Cuántas horas has realizado?: "))

# Preguntamos cuánto cuesta cada hora de trabajo
coste = int(input("Coste por hora del trabajo: "))

# Calculamos el coste final de todas las horas
total = str(horas * coste)

# Imprimimos ese cálculo
print("Importe total: " + total)