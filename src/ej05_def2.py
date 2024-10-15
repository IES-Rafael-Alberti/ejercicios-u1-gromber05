
def calcula_precio(precio: float, iva: float) -> str:
    iva = precio * iva
    importe = precio + iva
    return importe

def comprobar_iba(precio, iva) -> str:
    if iva in range(0, 1):
        final = calcula_precio(precio, iva)
    else:
        final = calcula_precio(precio, 0.21)
    return final

def main():
    precio = float(input('Introduce aquí el precio sin iva: '))
    iva = float(input("Introduce el IVA (21% = 0.21): "))
    
    importe = comprobar_iba(precio, iva)

    print(f"El precio final del artículo con IVA ({iva}) es {importe}€.")


if __name__ == "__main__":
    main()