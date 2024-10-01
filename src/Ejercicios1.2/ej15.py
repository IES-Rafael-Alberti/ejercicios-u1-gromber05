# Preguntamos cuánto dinero ha sido introducido en la cuenta
total = float(input('¿Cuánto dinero has introducido en la cuenta?: '))

# Calculamos el interes y el que se ha sumado a lo largo de los años
intereses = total * 0.04

interes_año1 = total + intereses
interes_año2 = interes_año1 + intereses
interes_año3 = interes_año2 + intereses

# Lo redondeamos a dos decimales
redondeo_año1 = round(interes_año1, 2)
redondeo_año2 = round(interes_año2, 2)
redondeo_año3 = round(interes_año3, 2)

# Imprimimos el resultado
print(f'El dinero introducido en la cuenta ha sido de {total}')
print(f'El dinero con intereses del primer año ha sido de {redondeo_año1}')
print(f'El dinero con intereses del segundo año ha sido de {redondeo_año2}')
print(f'El dinero con intereses del tercer año ha sido de {redondeo_año3}')
