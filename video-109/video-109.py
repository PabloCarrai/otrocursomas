#   Remover los valores duplicados de una lista.
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
print(f"Tengo la lista_original con el siguiente contenido {lista_original}")
lista_original=list(set(lista_original))
print(f"Si remuevo los duplicados obtengo {lista_original}")
