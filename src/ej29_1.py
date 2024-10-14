import random

def numeroaleatorio(a, b):
    return random.randint(a, b+1)



def comprobarnumero(num, num2):
    if num == num2:
        print("Error los números introducidos son iguales")
    elif num2 < num:
        return num, num2
    else:
        return num2, num

def main():
    num = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))

    num, num2 = comprobarnumero(num, num2)

    c = numeroaleatorio(num, num2)
    print(f'El número aletario entre {num} y {num2} es {c}')



if __name__ == "__main__":
    main()