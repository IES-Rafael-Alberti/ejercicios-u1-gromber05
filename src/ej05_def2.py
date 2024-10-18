
def calcula_precio(precio: float, iva: float) -> str:
    iva = comprobar_iba(iva)
    ivap = int(iva * 100)
    iva = precio * iva
    importe = precio + iva
    return f"El precio final del artículo con IVA ({ivap}%) es {importe}€."

def comprobar_iba(iva: float) -> str:
    if 0 < iva <= 1:
        return iva
    else:
        iva = 0.21
        return iva
    
def main():
    precio = float(input('Introduce aquí el precio sin iva: '))
    iva = float(input("Introduce el IVA (21% = 0.21): "))
    
    print(calcula_precio(precio, iva))


if __name__ == "__main__":
    main()