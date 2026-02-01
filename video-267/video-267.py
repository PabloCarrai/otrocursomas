#   Crear una funcion recursiva para sumar los numeros de una  lista


def sumar_lista(numeros):
    """
    Suma los elementos de una lista:

    :param numeros: Lista de valores numericos
    Returns:
    Retorna la suma de los valores de la lista
    """
    if len(numeros) == 0:
        return 0
    else:
        return numeros[0] + sumar_lista(numeros[1:])


valores = [1, 2, 3, 4, 5]
resultado = sumar_lista(valores)
print(resultado)


valores1 = []
resultado1 = sumar_lista(valores1)
print(resultado1)
