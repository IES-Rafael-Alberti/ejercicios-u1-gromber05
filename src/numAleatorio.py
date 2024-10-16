import random
import math

print(f'Bienvenido, solo tienes 5 intentos para averiguar el número, suerte')
print(f'Intento: 0')


def numAleatorio() -> int:
    numA = random.randint(0, 100)
    return numA

def comprobarAleatorio(numA: int, numB: int) -> bool:
    if numA == numB:
        return True
    if numA != numB:
        return False

def diferencia(numA: int, numB:int) -> int:

    i = abs(numA - numB)
    ale = ''
    if i > 75:
        ale = "Te congelas"
    elif i > 50:
        ale = "Un poquito de fresco"
    elif i > 30:
        ale = "Templaito"
    elif i > 20:
        ale = "Empieza a hacer calor"
    elif i > 10:
        ale = "Hace calorcillo"
    elif i > 5:
        ale = "TE QUEMAS"
    elif i >= 0:
        ale = "TE ESTÁS QUEMANDO"
    return ale
  

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
    global Configintentos
    
    if comprobacion is False:  

        for contador in range(0, 10):
            diferen = diferencia(numUsuario, numAdivinar)

            pos = posi(numUsuario, numAdivinar)
            if pos == True:
                pos2 = '>'
            elif pos == False:
                pos2 = '<'
            
            print(f'{pos2} {diferen}')

            final(numAdivinar)

        else: 
            print('Mala suerte, te quedaste sin intentos:')
    else:
        print('Felicidades!')
        exit()
    
def main():

    numAdivinar = numAleatorio()
    final(numAdivinar)

if __name__ == '__main__':
    main()