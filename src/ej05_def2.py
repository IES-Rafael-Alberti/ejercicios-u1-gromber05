
def calcula_precio(importe: float, iva: float) -> str:
    iva = importe * iva
    importe = importe + iva
    return f"El precio con iva ha sido un total de {importe} y el iva añadido ha sido un total de {iva}"


def main():
    precio = float(input('Introduce aquí el precio sin iva: '))
    iva = float(input("Introduce el IVA (21% = 0.21): "))
    
    if iva in range(0, 1):
        final = calcula_precio(precio, iva)
    else:
        final = calcula_precio(precio, 0.21)
    print(final)


if __name__ == "__main__":
    main()