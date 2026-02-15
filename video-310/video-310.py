#   Creacion de archivo texto plano


def main():
    nombre_archivo = "video-310/paises.txt"
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write("Colombia")
        f.write("\n")
        f.write("Ecuardor")
        f.write("\n")
        f.write("Argentina")
        f.write("\n")
        f.write("Alemania")
        f.write("\n")
        f.write("Peru")
        f.write("\n")
        f.write("Rusia")


if __name__ == "__main__":
    main()
