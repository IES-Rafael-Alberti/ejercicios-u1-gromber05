#
def comprobar_numero (cadena : str) -> bool:
    cadena = cadena.strip()
    return cadena.isdigit() or (cadena.startswith("-") and cadena[1:].isdigit())

def dame_entero() -> int:
    cadena = input("Dame un entero: ")
    comprobar_numero(cadena)
    while comprobar_numero(cadena) == False :
        cadena = input("**ERROR** NO ES UN ENTERO \n Dame un entero: ")
    return cadena


def main():
    num = dame_entero()
    print(f"Escribiste el número {num}")

if __name__ == "__main__":
    main()