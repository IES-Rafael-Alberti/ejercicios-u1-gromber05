
def comprobarPrimo(n: int) -> bool:
  for i in range(2,n):
    if (n % i) == 0:
      return False
  return True


def pedirNumero() -> int:
    num = input("Introduzca un número: ")
    while num == 0:
        return f"**ERROR** El número introducido no puede ser 0"
        num = input("Introduzca de nuevo un número: ")
    return num


def main():
    num = pedirNumero()
    a = comprobarPrimo(num)
    if a == False:
        print(f'El número {num} no es primo.')
    elif a == True:
        print(f'El número {num} es primo.')



if __name__ == "__main__":
    main()