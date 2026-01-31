#   Filtrar el contenido de una lista
print("#   Filtrar el contenido de una lista")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Contenidod de variable numeros {numeros}")
print(f"Cantidad elemento en lista numeros {len(numeros)}")


def extraer_impares(lista):
    impares = []
    for n in lista:
        if n % 2 != 0:
            impares.append(n)
    return impares


impares = extraer_impares(numeros)
print(f"Contenido de impares de numeros {impares}")
print(f"Cantidad elementos impares {len(impares)}")

#   Ahora con lambda
resultado1 = [n for n in numeros if n % 2 != 0]
print(f"Impares con lista de comprension {resultado1}")
print(f"Cantidad elementos impares {len(resultado1)}")
