#   Calcular la frecuencia(ocurrencias) de los elementos de una lista.
lista_original = [
    1,
    2,
    1,
    2,
    3,
    2,
    3,
    4,
    5,
    4,
    5,
    6,
    5,
    6,
    7,
    8,
    7,
    8,
    7,
    6,
    5,
    4,
    3,
    4,
    5,
    6,
]

print(f"Contenido de la lista {lista_original}")
print(f"Cantidad de elementos de lista {len(lista_original)}")

frecuencia = {}
for n in lista_original:
    if n in frecuencia:
        frecuencia[n] += 1
    else:
        frecuencia[n] = 1

print(f"El valor de la frecuencia es {frecuencia}")