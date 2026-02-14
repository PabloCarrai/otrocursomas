def main():
    print("Manipulacion de archivos")
    nombre_archivo = "video-308/lenguajes.txt"
    archivo = open(nombre_archivo, "r") #   Nombre del archivo y modo de lectura
    for linea in archivo.readlines():
        print(linea, end="")
    archivo.close()     #   Esto cierra el archivo abierto


if __name__ == "__main__":
    main()
