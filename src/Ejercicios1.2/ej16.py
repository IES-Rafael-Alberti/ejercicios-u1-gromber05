# Introducimos los valores con los que vamos a operar
pan = 3.49
pan_de_ayer = pan * 0.60

# Preguntamos cuantas barras de pan han sido vendidas y las asignamos a un valor
pan_ayer = int(input('¿Cuántas barras que no son del día has vendido?: '))

# Calculamos el precio total con el descuento y lo redondeamos a dos decimales
precio_con_descuento = pan_ayer * (pan - pan_de_ayer)
precio_total = round(precio_con_descuento, 2)

print(f'El precio normal de una barra de pan es de {pan}, el descuento por no ser fresca es de {pan_de_ayer} y en total, el precio por todas las barras de pan vendidas es un total de {str(precio_total)}')