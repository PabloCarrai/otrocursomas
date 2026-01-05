numeros = [1, 2, 4, 6, 8, 10, 14, 15, 16]
numeros.append(14)
numeros.append(14)
numeros.append(14)
numeros.append(14)
print(numeros)
#   Metodo count()
print(f"Cantidad de veces que aparece 14 en lista numero: {numeros.count(14)}")
#   Ocurrencias de 0 en numeros
ocurrencias = numeros.count(0)
print(f"Cantidad de veces que aparece 14 en lista numero: {ocurrencias}")
print(numeros)