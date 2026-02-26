from modelos.camion import Camion
from modelos.volqueta import Volqueta


def main():
    print("Clase volqueta")
    volqueta_carga = Volqueta("FGH-951", "Daewoo", 2014, "Taiwan", 4000, 2000000)
    print(f"Tipo de datos de volqueta_carga {type(volqueta_carga)}")
    print(f"Placa: {volqueta_carga.placa}")
    print(f"Marca: {volqueta_carga.marca}")
    print(f"Modelo: {volqueta_carga.modelo}")
    print(f"Pais: {volqueta_carga.pais_procedencia}")
    print(f"Capacidad: {volqueta_carga.capacidad_carga}")
    print(f"Costo: {volqueta_carga.costo_servicio}")
    print(f"Esta encendido? {"Si" if volqueta_carga.estado else "No"}")
    volqueta_carga.encender()
    print(f"Esta encendido? {"Si" if volqueta_carga.estado else "No"}")
    volqueta_carga.acelerar()
    volqueta_carga.frenar()
    volqueta_carga.encender()
    print(f"Esta encendido? {"Si" if volqueta_carga.estado else "No"}")
    volqueta_carga.cargar_material()
    volqueta_carga.acelerar()
    volqueta_carga.frenar()
    volqueta_carga.descargar_material()
    volqueta_carga.apagar()
    print(f"Esta encendido? {"Si" if volqueta_carga.estado else "No"}")


if __name__ == "__main__":
    main()
