
def resultado(num: int) -> str:
    if num >= 0:
        num = num + 1
        num = num * num
        num = num / 2
        
        return f"El resultado es: {num}"
    else:
        return f'El número introducido no puede ser negativo'
    
def pedirNumero() -> int:
    num = input("Introduzca un número: ")
    return num

def main():
    num = int(pedirNumero())
    calculo = resultado(num)
    print(calculo)

if __name__ == "__main__":
    main()