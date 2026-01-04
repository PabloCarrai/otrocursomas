numeros_primos = (2, 3, 5, 7, 11, 13, 17, 19)
print(f"Cantidad de elementos de la lista numeros_primos: {len(numeros_primos)}")
#   Iteracion con ciclo for
for elemento in range(len(numeros_primos)):
    print(
        f"El valor del elemento en el indice {elemento} es igual a {numeros_primos[elemento]}"
    )

# Otra forma
for n in numeros_primos:
    print(f"Valor {n}")
