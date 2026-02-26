from modelos.formula1 import Formula1


def main():
    print("Clase volqueta")
    coche_carrera = Formula1("ABR-451", "Mitsubishi", 2014, "Malasia", 120)
    print(f"Tipo de datos de coche_carrera: {type(coche_carrera)}")
    coche_carrera.competir()
    print(f"Placa: {coche_carrera.placa}")
    print(f"Marca: {coche_carrera.marca}")
    print(f"Modelo: {coche_carrera.modelo}")
    print(f"Pais: {coche_carrera.pais_procedencia}")
    print(f"Peso: {coche_carrera.peso}")
    print(f"Esta encendido? {"Si" if coche_carrera.estado else "No"}")


if __name__ == "__main__":
    main()
