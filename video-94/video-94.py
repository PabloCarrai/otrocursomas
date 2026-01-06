arco_iris = {"Rojo", "Naranja", "Amarillo", "Verde", "Azul", "Añil"}
print(f"Cantidad de elementos de la variable arco_iris {len(arco_iris)})")
arco_iris.add("Violeta")
print(f"Cantidad de elementos de la variable arco_iris {len(arco_iris)})")
#   Iteracion con enumarate()
for indice, color in enumerate(arco_iris):
    print(f"Indice {indice} Color {color}")
