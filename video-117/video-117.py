#   Realizar operaciones de union e interseccion de conjuntos.
colores = {"Rojo", "Verde", "Azul", "Naranja"}
colores_1 = {"Azul", "Purpura", "Verde", "Violeta", "Gris"}
# union
union_colores = colores.union(colores_1)
# interseccion
interseccion_colores = colores.intersection(colores_1)
print(f"El primer conjunto es colores, su contenido {colores}")
print(f"El segundo conjunto es colores_1, su contenido {colores_1}")
print(f"La union da {union_colores}")
print(f"La interseccion da {interseccion_colores}")
