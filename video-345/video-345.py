from modelos.camion import Camion


def main():
    print()
    #   Creacion/instanciacion de un objeto camion
    camion_carga = Camion("ABD-456", "Scania", 2015, "China", 2000)
    print(f"El tipo de dato de la variable camion_carga es {type(camion_carga)}")
    print(f"Placa: {camion_carga.placa}")
    print(f"Marca: {camion_carga.marca}")
    print(f"Modelo: {camion_carga.modelo}")
    print(f"Pais: {camion_carga.pais_procedencia}")
    print(f"Carga: {camion_carga.capacidad_carga}")
    print(f"Esta encendido? {"Si" if camion_carga.estado else "No"}")


if __name__ == "__main__":
    main()
