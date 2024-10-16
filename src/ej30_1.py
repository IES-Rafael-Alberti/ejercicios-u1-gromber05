"""
En esta función a la que llamaremos comprobarPrimo, le introducimos un valor y lo que nos devuelve es un valor booleano, o lo que es lo mismo,
si es primo nos devuelve True y si no es primo nos devueve False
"""
def comprobarPrimo(n) -> bool:
  for i in range(2,n):
    if (n % i) == 0:
      return False
  return True

"""
En esta función lo que hacemos es que nos pida un número y nos identifique si es 0, si el caso es verdadero
Lo que nos hace la función es que nos devuelve una cadena de texto.
"""
def pedirNumero():
    num = int(input("Introduzca un número: "))
    while num == 0:
        return f"**ERROR** El número introducido no puede ser 0"
        num = int(input("Introduzca de nuevo un número: "))
    return num

"""
En la función main lo que definimos es el proceso de pedir el número y comprobarlo para luego volver a tomar la variable e imprimir 
el resultado obtenido
"""
def main():
    num = pedirNumero()
    a = comprobarPrimo(num)
    if a == False:
        print(f'El número {num} no es primo.')
    elif a == True:
        print(f'El número {num} es primo.')



if __name__ == "__main__":
    main()