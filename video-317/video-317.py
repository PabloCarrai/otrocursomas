#   Operaciones adicionales

import os


def main():
    #   Operaciones adicionales sobre archivos
    print("Operaciones adicionales sobre archivos")
    print("Renombrar un archivo")
    nombre_archivo = "video-317/archivo.txt"
    if os.path.isfile(nombre_archivo):
        print(f"El archivo {nombre_archivo} existe en disco")
    else:
        print(f"El archivo {nombre_archivo} no existe en disco")

    print()
    os.rename(nombre_archivo, "video-317/archivo2.txt")

    if os.path.isfile(nombre_archivo):
        print(f"El archivo {nombre_archivo} existe en disco")
    else:
        print(f"El archivo {nombre_archivo} no existe en disco")


if __name__ == "__main__":
    main()
    print("Fin del programa")
