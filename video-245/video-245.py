#   Pasar argumento por referencia
print("Pasar argumento por referencia")


def agregar_elemento(lista):
    lista.append(2)


numero = [1]
print(f"Contenido de la lista numero: {numero}")
agregar_elemento(numero)  # Agrega un elemento a la lista
print(f"Contenido de la lista numero: {numero}")
