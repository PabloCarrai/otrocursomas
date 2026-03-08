from modelos.rectangulo import Rectangulo
from modelos.circulo import Circulo
from modelos.triangulo import Triangulo


def main():
    # Prueba ejecucion sobre jerarquia de herencia de figuras
    figuras = []
    rectangulo_rojo = Rectangulo("Rojo", "Negro", 10, 5)
    circulo_verde = Circulo("Verde", "Negro", 5)
    triangulo_negro = Triangulo("Negro", "Gris", 7, 10)
    figuras.append(rectangulo_rojo)
    figuras.append(circulo_verde)
    figuras.append(triangulo_negro)

    print()
    print("El area de todas las figuras: ")
    for f in figuras:
        f.dibujar()
        print()
        area = f.area()
        print(f"El area es igual a {area} unidades al 2")

    print()
    print("Demostracion de sobreescritura de metodos")
    print(rectangulo_rojo)  #   Invoca por defecto el metodo __str__

    print()
    print(circulo_verde)

    print()
    print(triangulo_negro)


if __name__ == "__main__":
    main()
