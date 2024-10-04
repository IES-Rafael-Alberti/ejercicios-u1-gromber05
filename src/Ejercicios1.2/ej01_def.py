# Primero definimos la funcion del saludo
def saludo(nom):
        return "Hola, " + nom + "."

# Establecemos la funcion main que pedirá el nombre
def main():
        nombre = input("Escribe tú nombre: ")
        print(saludo(nombre))

if __name__ == "__main__":
        main()
        