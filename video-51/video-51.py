valores = "2,3,5,7,11"


#   Creacion de una funcion(proceso) para buscar una cadena dentro de otra
def encontrar(cadena, caracter):
    indice = -1
    for i in range(0, len(cadena)):
        if caracter == cadena[i]:
            indice = i
            break
    return indice


indice = encontrar(valores, "3")
print(f"El indice del elemento 3 es igual a {indice}")
print(valores[indice])

indice = encontrar(valores, "8")
print(f"El indice del elemento 8 es igual a {indice}")
print(valores[indice])
