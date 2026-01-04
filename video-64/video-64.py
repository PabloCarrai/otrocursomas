#   Iteraciones en lista
#   Ciclo while
numeros = [1, 4, 6, 8, 10]
i = 0
while i < len(numeros):
    print(f"El indice vale {i} - Valor del elemento {numeros[i]}")
    i += 1
# iteracion de lista con ciclo while del ultimo elemento al primero
i = (
    len(numeros) - 1
)  # El problema era que la cantidad de elemento de la lista es mayor a la real, por eso necesitamos uno menos
while i >= 0:
    print(f"El indice vale {i} - Valor del elemento {numeros[i]}")
    i -= 1
