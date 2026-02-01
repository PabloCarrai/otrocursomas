#   Tomar una lista de numeros e identificar los numeros unicos


def identificarUnicos(lista):
    """
    Obtiene una lista con los elementos unicos.

    :param lista: Lista que se analiza para obtener los elementos unicos
    Returns:
    Devuelve una lista con los elementos unicos.
    """
    if isinstance(lista, (tuple, list)):
        listaUnicos = []
        for elemento in lista:
            if elemento not in listaUnicos:
                listaUnicos.append(elemento)
        return listaUnicos
    else:
        raise TypeError("El argumento tiene que ser una lista o una tupla")


#   Primer prueba
try:
    listaPrueba = [1, 2, 1, 2, 3, 4, 3, 4, 5, 6, 67, 8, 9, 22]
    resultado = identificarUnicos(listaPrueba)
    print(f"La lista original es: {listaPrueba}")
    print(f"El resultado es {resultado}")
except TypeError as e:
    print(f"Error {e}")


#   Da error por pasar un string y no una lista/tupla
try:
    listaPrueba1 = "1, 2, 1, 2, 3, 4, 3, 4, 5, 6, 67, 8, 9, 22"
    resultado1 = identificarUnicos(listaPrueba1)
    print(f"La lista original es: {listaPrueba1}")
    print(f"El resultado es {resultado1}")
except TypeError as e:
    print(f"Error {e}")

#   Otro caso con lista
try:
    listaPrueba2 = [22, 2.8, 2.7, 2.9, 2.8, 2.8, 3, 3.3, 3.3, 3.4, 3.5, -35.69, -35, 39]
    resultado2 = identificarUnicos(listaPrueba2)
    print(f"La lista original es: {listaPrueba2}")
    print(f"El resultado es {resultado2}")
except TypeError as e:
    print(f"Error {e}")


#   Con tuplas
try:
    listaPrueba3 = (3.3, 3.3, 3.4, 3.5, -35.69, -35, 39)
    resultado3 = identificarUnicos(listaPrueba3)
    print(f"La lista original es: {listaPrueba3}")
    print(f"El resultado es {resultado3}")
except TypeError as e:
    print(f"Error {e}")


#   Con tuplas
try:
    listaPrueba4 = [2, 5, 2, 2, 3, 7, 5, 7, 11, 13]
    resultado4 = identificarUnicos(listaPrueba4)
    print(f"La lista original es: {listaPrueba4}")
    print(f"El resultado es {resultado4}")
except TypeError as e:
    print(f"Error {e}")
