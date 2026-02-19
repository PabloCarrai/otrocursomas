from modelos.carro import Carro


def main():
    fitito = Carro("B406-HC-3", "Mercedez", 2015, "Brazil")  # creacion de objeto carro
    print()
    print(f"El tipo de datos de la variable fitito es: {type(fitito).__name__}")
    print(f"Placa del coche {fitito.placa}")
    print(f"Marca del coche {fitito.marca}")
    print(f"Modelo del coche {fitito.modelo}")
    print(f"Procedencia del coche {fitito.pais_procedencia}")
    print(f"Estado del coche {"Si" if fitito.estado else "No"}")
    print()
    print("invocacion de metodos de carro")
    fitito.encender()
    print(f"Estado del coche {"Si" if fitito.estado else "No"}")
    fitito.apagar()
    print(f"Estado del coche {"Si" if fitito.estado else "No"}")
    fitito.encender()
    print(f"Estado del coche {"Si" if fitito.estado else "No"}")    
    fitito.acelerar()
    fitito.frenar()
    print(f"Estado del coche {"Si" if fitito.estado else "No"}")  

if __name__ == "__main__":
    main()
