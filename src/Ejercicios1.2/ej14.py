# Introducimos los valores
peso_payasos = 112
peso_muñecas = 75

# Preguntamos la cantidad de ambos y lo asignamos cada una a un valor
muñecas = int(input('¿Cuántas muñecas han sido vendidas?: '))
payasos = int(input('¿Cuántos payasos han sido vendidos?: '))

# Realizamos el calculo necesario
calculo_payasos = peso_payasos * payasos
calculo_muñecas = peso_muñecas * muñecas
total = calculo_payasos + calculo_muñecas
total_kilos = float(total /  1000)

# Imprimimos el resultado
print(f'El paquete que va a ser enviado tiene un peso total de {total} gramos o {total_kilos} kilogramos')