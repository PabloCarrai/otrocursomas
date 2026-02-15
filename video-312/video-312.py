def main():
    #   Creacion de Archivos binarios
    print("Creacion de Archivos binarios")
    nombre_archivo = "video-312/numeros.bin"
    archivo = open(nombre_archivo, "wb")  # w es escritora b es binario
    numeros = [2, 3, 5, 7, 11]
    archivo.write(bytearray(numeros))  #   Escribe la lista al archivo
    archivo.close()
    print("Programa terminado")


if __name__ == "__main__":
    main()
