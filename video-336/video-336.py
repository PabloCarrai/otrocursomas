from modelos.carro import Carro


def main():
    fitito = Carro("B406-HC-3", "Mercedez", 2015, "Brazil")  # creacion de objeto carro
    print(f"El tipo de datos de la variable fitito es :{type(fitito)}")


if __name__ == "__main__":
    main()
