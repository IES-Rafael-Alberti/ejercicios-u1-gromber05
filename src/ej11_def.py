
def resultado(num: int) -> int or bool:
    if num >= 0:
        num = num + 1
        num = num * num
        num = num / 2
        
        return num
    else:
        return False
    
def pedirNumero() -> int:
    num = input("Introduzca un número: ")
    return num

def main():
    num = int(pedirNumero())
    calculo = resultado(num)
    if calculo == False:
        print("El número introducido no puede ser negativo")
    else:
        print(f"El resultado es: {calculo}")

if __name__ == "__main__":
    main()