numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#   Suma de impares
e = 0
sumaImpares = 0
while e < len(numeros):
    if numeros[e] % 2 == 1:
        sumaImpares += numeros[e]
    e += 1

print(f"numeros es {numeros}")
print(f"La suma de impares es {sumaImpares}")
