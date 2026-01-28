#   Error al intentar abrir un archivo inexistente
print("Error al intentar abrir un archivo inexistente")
nombre_archivo = "python.txt"
try:
    with open(nombre_archivo, "r") as f:
        for l in f.readlines():
            print(l)
except FileNotFoundError as e:
    print(f"Error: {e}")
