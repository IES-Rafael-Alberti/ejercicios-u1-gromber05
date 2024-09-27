
peso = float(input('¿Cuánto pesas?: '))
estatura = float(input('¿Cuánto mides?: '))

o1 = estatura * estatura
IMC = peso / o1
IMC_final = round(IMC, 2)

print('Tu índice de masa corporal es de: ' + str(IMC_final))
