#   Manipulacion de archivos
print("Manipulacion de archivos")
nombre_archivo = "video-308/lenguajes.txt"
archivo = open(nombre_archivo, "r")
for linea in archivo.readlines():
    print(linea, end="")
