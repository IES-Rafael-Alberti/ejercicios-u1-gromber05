
def resultado(num):
    return f"El resultado es: {num}"

def main():
    num = int(input('Introduzca un número: '))
    if num >= 0:
        num = num + 1
        num = num * num
        num = num / 2
        
        print(resultado(num))
    else:
        print("El número introducido no puede ser negativo")

if __name__ == "__main__":
    main()