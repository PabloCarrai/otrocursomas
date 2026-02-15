def main():
    print("Adicionar contenido a archivo plano")
    nombre_archivo = "video-311/paises.txt"
    with open(nombre_archivo, "a+", encoding="utf-8") as f:  # a+ es de append(agregar)
        f.write("\n")
        f.write("Egipto")
        f.write("\n")
        f.write("Japon")
        f.write("\n")
        f.write("Bolivia")


if __name__ == "__main__":
    main()
