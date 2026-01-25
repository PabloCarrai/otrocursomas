#
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sumaInpares = 0
for i in range(len(numeros)):
    if numeros[i] % 2 == 1:  #   Otra forma de sacar un impar
        sumaInpares += numeros[i]

print(f"Cantidad de elementos en numeros {numeros}")
print(f"Suma de impares de numeros {sumaInpares}")
