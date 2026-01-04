#   operaciones basicas que prove la clase tuple()
colores = ("Negro", "Blanco", "Negro", "Azul", "Rojo", "Verde")
print(
    f"Cantidad de apariciones del color Negro en Colores: {colores.count("Negro")}"
)  # Contamos las apariciones en colores de Negro

print(
    f"Cantidad de apariciones del color negro en Colores: {colores.count("negro")}"
)  # Ahora es apariciones de negro
#   Metodo index(devuelve el incide de un elemento)
print(f"Indice del color Rojo en Colores: {colores.index("Rojo")}")
print(f"Indice del color Negro en Colores: {colores.index("Negro")}")
