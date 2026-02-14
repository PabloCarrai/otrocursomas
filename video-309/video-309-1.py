def main():

    print("Apertura de un archivo con un manejador de contexto:")

    nombre_archivo = "video-308/lenguajes.txt"
    with open(nombre_archivo, "r") as f:
        for e in f.readlines():
            print(e, end="")


if __name__ == "__main__":
    main()
