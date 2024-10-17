
def calcula_precio(precio: float, iva: float) -> str:
    iva = comprobar_iba(iva)

    iva = precio * iva
    importe = precio + iva
    return importe

def comprobar_iba(iva: float) -> str:
    if 0 < iva <= 1:
        return iva
    else:
        iva = 0.21
        return iva
    
def main():
    precio = float(input('Introduce aquí el precio sin iva: '))
    iva = float(input("Introduce el IVA (21% = 0.21): "))
    
    importe = calcula_precio(precio, iva)

    ivap = comprobar_iba(iva)
    print(f"El precio final del artículo con IVA ({ivap}%) es {importe}€.")


if __name__ == "__main__":
    main()