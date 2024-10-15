"""

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