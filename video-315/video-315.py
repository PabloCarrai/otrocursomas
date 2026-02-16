#   Modulo pickle

import pickle


def main():
    #   Uso del modulo pickle para serializar y des-serializar objetos python
    print("Uso del modulo pickle para serializar y des-serializar objetos python")
    paises_capitales = {
        "Colombia": "Bogota",
        "Ecuador": "Quito",
        "Argentina": "Buenos Aires",
    }
    nombre_archivo = "video-315/paises_capitales.pickle"
    with open(nombre_archivo, "wb") as f:
        pickle.dump(paises_capitales,f)

    print("El programa ha terminado")


if __name__ == "__main__":
    main()
