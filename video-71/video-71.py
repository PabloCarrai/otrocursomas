numeros = [1, 2, 4, 6, 8, 10, 14, 15, 16]
print(numeros)
#   Metodo pop()
ultimo_elemento = numeros.pop()  # elimina el ultimo elemento y lo muestra
print(ultimo_elemento)
print(f"Se ha eliminado el ultimo_elemento {ultimo_elemento} de la lista numeros")
print(numeros)

#   Usando un indice con pop
ocho = numeros.pop(numeros.index(8))
print(f"Eliminamos el indice del elemento 8 {ocho}")
print(numeros)

#   Eliminar ultimo elemento usando pop y indice negativo
ultimo_elemento = numeros.pop(-1)
print(ultimo_elemento)
print(f"Se ha eliminado el ultimo_elemento {ultimo_elemento} de la lista numeros")
print(numeros)

#   Eliminar un elemento con pop con un indice inexistente(IndexError: pop index out of range)
#numeros.pop(20)
