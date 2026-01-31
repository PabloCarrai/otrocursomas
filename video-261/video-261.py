#   Crear una funcion para sumar todos los numeros en una lista o tupla:


def sumarNumeros(numeros):
    """
    Realiza una suma de todos los elementos de una lista o tupla

    :param numeros: Descripción

    Returns: Devuelve total con la sumatoria de todos los elementos
    """
    if isinstance(numeros, (tuple, list)):
        total = 0
        for n in numeros:
            total += n
        return total
    else:
        raise ValueError("Ha pasado un argumento que no es lista ni tupla")


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
tupla = (16, 17, 18, 19, 20)


try:
    sumaLista = sumarNumeros(lista)
    print(f"La lista original es {lista}")
    print(f"Sumando sus elementos tenemos {sumaLista}")
except ValueError as e:
    print(f"Se produjo un error {e}")

try:
    sumarTupla = sumarNumeros(tupla)
    print(f"La tupla original es {tupla}")
    print(f"Sumando sus elementos tenemos {sumarTupla}")
except ValueError as e:
    print(f"Se produjo un error {e}")
