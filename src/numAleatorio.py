import random
import math

contador = 0
print(f'Bienvenido, solo tienes 5 intentos para averiguar el número, suerte')
print(f'Intento: 0')

def numAleatorio():

    numA = random.randint(0, 100)
    return numA

def comprobarAleatorio(numA: int, numB: int) -> bool:

    if numA == numB:
        return True
    if numA != numB:
        return False

def diferencia(numA: int, numB:int) -> int:

    i = abs(numA - numB)

    if i > 75:
        ale = "Te congelas"
    elif i > 50:
        ale = "Un poqutio de fresco"
    elif i > 30:
        ale = "Templaito"
    elif i > 20:
        ale = "Empieza a hacer calor"
    elif i > 10:
        ale = "Hace calorcillo"
    elif i > 5:
        ale = "TE QUEMAS"
    
    pose = posi(numA, numB)
    print(f'{ale} {pose}')
    
def intentos():

    global contador
    contador = contador + 1
    print(f'Intento: {contador}')

def posi(numA: int, numB: int) -> bool:

    if numA > numB:
        return True
    elif numA < numB:
        return False


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
    
    
def main():
    
    numAdivinar = numAleatorio()
    numUsuario = pedirNumero()

    comprobarAleatorio = False
    global contador

    if comprobarAleatorio == False:
        for contador in range(0,4):

            diferencia = diferencia(numUsuario, numAdivinar)

            posi = posi(numUsuario, numAdivinar)
            if posi() == True:
                posi = '>'
            elif posi() == False:
                posi = '<'
            
            print(f'{posi} {diferencia}')

            numUsuario = pedirNumero()
    
        else: 
            print('Mala suerte, te quedaste sin intentos:')
    else:
        print('Felicidades!')
"""
intentos()
        diferencia(numA, numB)
"""
if __name__ == '__main__':
    main()