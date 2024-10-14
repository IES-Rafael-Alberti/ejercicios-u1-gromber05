import math

def comprobar_numero(valor: str):
    if valor[:1] == "-":
       valor = valor[1:]

    if tiene_mas_de_un_punto(valor):
        return False
    
    return contiene_solo_digitos_y_un_punto(valor)

def tiene_mas_de_un_punto(valor: str):       
    pos_punto = valor.find(".")
    if pos_punto >= 0 and valor.find(".", pos_punto + 1):
        return False
    else:
        return True

def contiene_solo_digitos_y_un_punto(valor: str):
    for i in range(len(valor), ): # 0..len(valor) - 1
        if not (valor[i].isdigit() or valor[i] == "."):
            return False
        else:
            return True

def calcular_area(a, b, c):
    semiperimetro = (a + b + c) / 2
    area = math.sqrt(semiperimetro * (semiperimetro - a) * (semiperimetro - b) * (semiperimetro - c))
    return area


def introduce_numero(msj: str):
    numero = input(msj).strip()
    while comprobar_numero(numero) == False:
        print("Error")
        numero = input(msj).strip()

    return float(numero)

def main():
    print("Dame los tres lados de un triángulo...")

    a = introduce_numero("")
    b = introduce_numero("")
    c = introduce_numero("")

    calcular_area(a, b, c)

if __name__ == "__main__":
    main()