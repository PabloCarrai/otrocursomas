numeros = [1, 4, 6, 8, 10]
#   Operaciones sobre lista

print(f"Contenidos de la lista numeros {numeros}")
print(f"Cantidad de elementos en numeros {len(numeros)}")
#   Agregar elementos en la lista con append()
numeros.append(14)
numeros.append(16)
print(f"Cantidad de elementos en numeros {len(numeros)}")
print(f"Contenidos de la lista numeros {numeros}")
#   Otra forma usando insert()
numeros.insert(1, 2)  # agrega un elemento en un indice, lista.insert(indice,elemento)
print(f"Contenidos de la lista numeros {numeros}")
#   usando insert con indices negativos
numeros.insert(-1, 15)
print(f"Contenidos de la lista numeros {numeros}")
