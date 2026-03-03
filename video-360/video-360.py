from modelos.pato import Pato
from modelos.gato import Gato
from modelos.perro import Perro


def main():
    animales = []
    cua = Pato("Platy", 2, "Anas platyrhunchos Domesticus", "Verde")
    charlie = Gato("Charly", 1, "Felis catus", True)
    mateo = Perro("Mateo", 2, "Canis lupus familiaris", "Golden Retiever")
    animales.append(cua)
    animales.append(charlie)
    animales.append(mateo)

    for animal in animales:
        print(f"El nombre del animal es {animal.nombre}")

    for animal in animales:
        print(animal.hablar())


if __name__ == "__main__":
    main()
