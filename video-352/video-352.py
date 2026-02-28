#   Polimorfismo
from modelos.formula1 import Formula1


def main():
    print("Clase volqueta")
    coche_carrera = Formula1("ABR-451", "Mitsubishi", 2014, "Malasia", 120)
    coche_carrera.encender()
    print(f"Esta encendido? {"Si" if coche_carrera.estado else "No"}")
    coche_carrera.acelerar()
    coche_carrera.competir()
    coche_carrera.frenar()
    coche_carrera.apagar()
    print(f"Esta encendido? {"Si" if coche_carrera.estado else "No"}")


if __name__ == "__main__":
    main()
