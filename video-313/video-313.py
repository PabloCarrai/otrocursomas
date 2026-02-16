# Lectura archivo binario


def main():
    print("Lectura de un archivo binario")
    nombre_archivo = "video-313/numeros.bin"
    archivo = open(nombre_archivo, "rb")
    numeros = list(archivo.read())
    print(numeros)
    archivo.close()


if __name__ == "__main__":
    main()
