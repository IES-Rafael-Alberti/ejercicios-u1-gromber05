
"""
En este programa lo que hacemos es calcular un numero aleatorio
"""
import random
import math

print(f'Bienvenido, solo tienes 5 intentos para averiguar el número, suerte.')
print(f'Intento: 1')

contador = 0
max_aciertos = 5

def numAleatorio() -> int:
    numA = random.randint(0, 100)
    return numA

def comprobarAleatorio(numA: int, numB: int) -> bool:
    if numA == numB:
        return True
    if numA != numB:
        return False

def diferencia(numA: int, numB:int) -> int:

    diferen = abs(numA - numB)
    pista = ''
    
    if diferen > 75:
        pista = "Te congelas"
    elif diferen > 50:
        pista = "Un poquito de fresco"
    elif diferen > 30:
        pista = "Templadito"
    elif diferen > 20:
        pista = "Empieza a hacer calor"
    elif diferen > 10:
        pista = "Hace calorcillo"
    elif diferen > 5:
        pista = "TE QUEMAS"
    elif diferen >= 0:
        pista = "TE ESTÁS QUEMANDO"
    return pista
  

def posi(numA: int, numB: int) -> bool:

    if numA > numB:
        return False
    elif numA < numB:
        return True

def pedirNumero() -> int:

    num = int(input(f'Introduce un número: '))
    comprobarNum(num)
    while num not in range(0, 100):
        print('**ERROR** El número introducido debe estar entre 0 y 100')
        num = int(input(f'Introduce un número: '))
    else:
        return num
    
def comprobarNum(num: str) -> int:
    num = str(num)
    if num.isdigit:
        num = int(num)
        return num
    else:
        print('**ERROR** El número introducido debe ser un número')

def final(numAdivinar: int):

    numUsuario = pedirNumero()
    comprobacion = comprobarAleatorio(numUsuario, numAdivinar)
    global contador
    global max_aciertos
    
    if comprobacion is False:  

        while contador < (max_aciertos - 1):
            diferen = diferencia(numUsuario, numAdivinar)

            pos = posi(numUsuario, numAdivinar)
            if pos == True:
                pos2 = 'está en mayor posición'
            elif pos == False:
                pos2 = 'está en menor posición'
            contador += 1
            print(f'{diferen} y {pos2}')
            print(f'Intento: {contador + 1}')
            final(numAdivinar)

        else: 
            print('Mala suerte, te quedaste sin intentos.')
            exit()
    else:
        print('¡Felicidades!')
        exit()
    
def main():

    numAdivinar = numAleatorio()
    final(numAdivinar)

if __name__ == '__main__':
    main()