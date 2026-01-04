numeros = [1, 2, 4, 6, 8, 10, 14, 15, 16]
#   Metodo remove() para eliminar elementos de una lista
print(f"Contenidos de la lista numeros {numeros}")
numeros.remove(1)  #  lista.remove(elemento) elimina primer aparicion de elemento
print(f"Contenidos de la lista numeros {numeros}")
#   que ocurre al intentar eliminar el mismo elemento(ValueError: list.remove(x): x not in list)
# numeros.remove(1)
print(f"Contenidos de la lista numeros {numeros}")
