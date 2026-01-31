#   Crear una funcion para multiplicar todos los numeros en una lista o tupla


def multiplicarNumeros(numeros):
    """
    Realiza una multiplicacion de todos los elementos de una lista o tupla

    :param numeros: lista o tupla con numeros

    Returns: Devuelve total con la multiplicacion de todos los elementos
    """
    if isinstance(numeros, (tuple, list)):
        total = 1
        for n in numeros:
            total *= n
        return total
    else:
        raise ValueError("Ha pasado un argumento que no es lista ni tupla")


lista = [1, 2, 3, 4]
tupla = (16, 17, 20)


try:
    resultadoMultiplicarLista = multiplicarNumeros(lista)
    print(f"La lista tiene los siguientes valores {lista}")
    print(f"Multiplicados quedaria {resultadoMultiplicarLista}")
except ValueError as e:
    print(f"Error {e}")


try:
    resultadoMultiplicarTupla = multiplicarNumeros(tupla)
    print(f"La lista tiene los siguientes valores {tupla}")
    print(f"Multiplicados quedaria {resultadoMultiplicarTupla}")
except ValueError as e:
    print(f"Error {e}")


prueba = "Locura"


try:
    resultadoMultiplicarprueba = multiplicarNumeros(prueba)
    print(f"La lista tiene los siguientes valores {prueba}")
    print(f"Multiplicados quedaria {resultadoMultiplicarprueba}")
except ValueError as e:
    print(f"Error {e}")
