arco_iris = {"Rojo", "Naranja", "Amarillo", "Verde", "Azul", "Añil"}
#   Operacion de subconjuntos
colores = {"Rojo", "Verde", "Azul"}
resultado = colores.issubset(arco_iris)
colores.add("Gris")  #   Agrego otro color

#   Union
mas_colores = arco_iris.union(colores)
print(f"Elementos de mas_colores {mas_colores})")
print(f"Cantidad de elementos de la variable mas_colores {len(mas_colores)})")
print(f"Tipo de dato variable mas_colores {type(mas_colores)})")

# Interseccion  Los que tienen en comun
interseccion = colores.intersection(arco_iris)
print(f"Elementos de interseccion {interseccion})")
print(f"Cantidad de elementos de la variable interseccion {len(interseccion)})")
print(f"Tipo de dato variable interseccion {type(interseccion)})")
