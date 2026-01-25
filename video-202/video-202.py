numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sumaInPar = 0
# sumar elementos pares

#  Para cada elemento en numeros
for n in numeros:
    if n % 2 == 1:
        sumaInPar += n
print("------------------------------------------------")
print(f"Numeros tiene {numeros}")
print("------------------------------------------------")
print(f"La suma de impares es {sumaInPar}")
print("------------------------------------------------")

#   Listas de comprension
print("------------------------------------------------")
print("Lista de comprension")
total = [numeros[i] for i in range(len(numeros))]
print(f"Contenido de total  {total}")
total=sum([numeros[i] for i in range(len(numeros))])
print(f"Contenido de total  {total}")