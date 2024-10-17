
# Pedimos el peso y la estatura para calcular el IMC
peso = float(input('¿Cuánto pesas?: '))
estatura = float(input('¿Cuánto mides?: '))

# Hacemos el calculo necesario del IMC y lo redondeamos a dos decimales
o1 = estatura * estatura
IMC = peso / o1
IMC_final = round(IMC, 2)

# Imprimimos el resultado
print('Tu índice de masa corporal es de: ' + str(IMC_final))
