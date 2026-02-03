def sumar(valor, valor1):
    """
    Realiza la suma de dos valores

    :param valor: Primer valor a sumar
    :param valor1: Segundo Valor a sumar

    returns:
    Devuelve la suma de valor y valor1
    """
    if isinstance(valor, (int, float)) and isinstance(valor1, (int, float)):
        return valor + valor1
    else:
        raise ValueError("Los argumentos tienen que ser enteros o real")


def restar(valor, valor1):
    """
    Realiza la resta de dos valores

    :param valor: Primer valor a resta
    :param valor1: Segundo Valor a resta

    returns:
    Devuelve la resta de valor y valor1
    """
    if isinstance(valor, (int, float)) and isinstance(valor1, (int, float)):
        return valor - valor1
    else:
        raise ValueError("Los argumentos tienen que ser enteros o real")


def multiplicar(valor, valor1):
    """
    Realiza la multiplicacion de dos valores

    :param valor: Primer valor a multiplicar
    :param valor1: Segundo Valor a multiplicar

    returns:
    Devuelve la multiplicacion de valor y valor1
    """
    if isinstance(valor, (int, float)) and isinstance(valor1, (int, float)):
        return valor * valor1
    else:
        raise ValueError("Los argumentos tienen que ser enteros o real")


def dividir(valor, valor1):
    """
    Realiza la division de dos valores

    :param valor: Primer valor a division
    :param valor1: Segundo Valor a division(no puede ser igual a 0)

    returns:
    Devuelve la division de valor y valor1
    """
    if isinstance(valor, (int, float)) and isinstance(valor1, (int, float)):

        if valor1 == 0:
            raise ZeroDivisionError("No se puede dividir por 0")
        else:
            return valor / valor1
    else:
        raise ValueError("Los argumentos tienen que ser enteros o real")
