def calcular_iva(precio, iva):
    iva = precio * iva
    precio = precio + iva
    return precio

def main():
    precio = float(input('Dime el precio sin IVA del producto: ' ))
    iva = float(input('Dime el porcentaje de IVA que has pagado (21% : 0.21): ' ))
    precio = calcular_iva(precio, iva)
    print(f"El precio final es de: {precio}")
    
if __name__ == "__main__":
    main()