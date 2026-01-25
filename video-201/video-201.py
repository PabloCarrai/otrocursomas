numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sumaPar = 0
# sumar elementos pares

#  Para cada elemento en numeros
for n in numeros:
    if n % 2 == 0:
        sumaPar += n
print("------------------------------------------------")
print(f"Numeros tiene {numeros}")
print("------------------------------------------------")
print(f"La suma de pares es {sumaPar}")
print("------------------------------------------------")
