#   Ciclo while
numeros = [1, 2, 3, 4, 5]
#   Suma de elementos de una lista.
total = 0
i = 0
while i < len(numeros):
    total += numeros[i]
    i += 1
print(f"La suma de los elementos de numero es {total}")

numeros.append(6)
numeros.append(7)
numeros.append(8)
numeros.append(9)
numeros.append(10)

print(f"Contenido de numeros {numeros}")

#   Suma de valores pares en numero
sumaPares = 0
e = 0
while e < len(numeros):
    if numeros[e] % 2 == 0:
        sumaPares += numeros[e]
    e += 1

print(f"numeros {sumaPares}")
