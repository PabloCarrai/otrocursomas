# Funcion fobinacci
def fibonacci_iterativo(n):
    """
    Calcula el n-esimo valor de la serie fibonacci enfoque iterativo
    :param n: valor de la serie fibonacci a calcular
    :returns: valor de la serie fibonacci
    """
    a = 0
    b = 1
    for i in range(n-1):
        a, b = b, a + b
    return b


def fibonacci_recursiva(n):
    """
    Calcula el n-esimo valor de la serie fibonacci enfoque recursivo
    :param n: valor de la serie fibonacci a calcular
    :returns: valor de la serie fibonacci
    """

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursiva(n - 2) + fibonacci_recursiva(n - 1)


resultado=fibonacci_iterativo(10)
print(f"Fibonacci iterativo {resultado}")


resultado=fibonacci_recursiva(10)
print(f"Fibonacci recursivo {resultado}")