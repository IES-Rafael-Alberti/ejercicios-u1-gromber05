
peso_payasos = 112
peso_muñecas = 75

muñecas = int(input('¿Cuántas muñecas han sido vendidas?: '))
payasos = int(input('¿Cuántos payasos han sido vendidos?: '))

calculo_payasos = peso_payasos * payasos
calculo_muñecas = peso_muñecas * muñecas

total = calculo_payasos + calculo_muñecas

total_kilos = float(total /  1000)

print(f'El paquete que va a ser enviado tiene un peso total de {str(total)} gramos o {str(total_kilos)} kilogramos')