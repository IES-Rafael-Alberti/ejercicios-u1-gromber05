
# Te pide la fecha de nacimiento y te lo separa
fecha = input("Ingrese su fecha de nacimiento (DD/MM/AA): ")
componentes = fecha.split('/')

# Mide si el formato es incorrecto
if len(componentes) != 3:
    print("Formato de fecha incorrecto. Asegúrate de usar dd/mm/aaaa.")
else:
    # Lo separa por dia, mes y año
    dia = componentes[0].zfill(2)
    mes = componentes[1].zfill(2)
    año = componentes[2]

    print(f"Día: {dia}")
    print(f"Mes: {mes}")
    print(f"Año: {año}")