from modelos.camion import Camion
from modelos.deportivo import Deportivo


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
    camion_carga.encender()
    print(f"Esta encendido? {"Si" if camion_carga.estado else "No"}")
    camion_carga.apagar()
    print(f"Esta encendido? {"Si" if camion_carga.estado else "No"}")
    camion_carga.cargarMercancia()
    camion_carga.descargarMercancia()

    print("Clase Deportiva")
    deportivo_lujo = Deportivo(
        "DEF-4789", "Audi", 2013, "Alemania", "Marca-Rines", "Deportivo"
    )
    print(f"Tipo de dato de deportivo_lujo {type(deportivo_lujo)}")
    print(f"Placa: {deportivo_lujo.placa}")
    print(f"Marca: {deportivo_lujo.marca}")
    print(f"Modelo: {deportivo_lujo.modelo}")
    print(f"Pais: {deportivo_lujo.pais_procedencia}")
    print(f"Esta encendido? {"Si" if deportivo_lujo.estado else "No"}")
    print(f"Rines: {deportivo_lujo.marca_rines}")
    print(f"Tipo: {deportivo_lujo.tipo}")


if __name__ == "__main__":
    main()
