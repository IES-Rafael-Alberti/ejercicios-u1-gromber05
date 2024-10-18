
def saludo(nom: str) -> str:
        return "Hola, " + nom + "."


def main():
        nombre = input("Escribe tú nombre: ")
        print(saludo(nombre))

if __name__ == "__main__":
        main()
        