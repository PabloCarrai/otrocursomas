#   Diferencia simetrica entre dos conjuntos
colores = {"Rojo", "Verde", "Azul", "Naranja"}
colores_1 = {"Azul", "Purpura", "Verde", "Violeta", "Gris"}
# Diferencia simetrica
diferencia_colores = colores.symmetric_difference(colores_1)
print(f"El primer conjunto es colores, su contenido {colores}")
print(f"El segundo conjunto es colores_1, su contenido {colores_1}")
print(f"La diferencia da {diferencia_colores}")
