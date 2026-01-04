numeros = [1, 4, 6, 8, 10]
#   Otra forma de iterar listas
for i in range(len(numeros)):
    print(f"Indice {i} Valor en numeros: {numeros[i]}")


for i in range(
    len(numeros) - 1, -1, -1
):  # hace decrementos(desde el total de elementos -1 hasta -1 haciendo -1 por cada elemento)
    print(f"Indice {i} Valor en numeros: {numeros[i]}")
