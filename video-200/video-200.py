#   Iteracion con for por elemento(ciclo for mejorado)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
# Ireacion con ciclo for mejorado(sin usar indice, por elementos)
for (
    n
) in (
    numeros
):  # Aca cada elemento en numero va a ser i, Es decir tomamos los elementos y se guarda en i
    print(f"El valor actual de n es {n}")
    total += n
print("------------------------------------------------")
print(f"Numeros tiene {numeros}")
print("------------------------------------------------")
print(f"La suma de {total}")
print("------------------------------------------------")
