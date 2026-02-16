#   leer el contenido de un archivo pickle
import pickle


def main():
    print("leer el contenido de un archivo pickle")
    nombre_archivo = "video-316/paises_capitales.pickle"
    with open(nombre_archivo, "rb") as f:
        paises_capitales_recuperados = pickle.load(f)
        print(
            f"tipo de datos de la variable de paises_capitales_recuperados, {type(paises_capitales_recuperados)}"
        )
        print(f"{paises_capitales_recuperados}")


if __name__ == "__main__":
    main()
