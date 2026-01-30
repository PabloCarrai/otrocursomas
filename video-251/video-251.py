#   Recursividad en funciones
print("Recursividad en funciones")


def factorial_iterativo(n):
    """
    Calcula factorial de un numero(enfoque interativo)
    Parameters:
    n: Numero de factorial a calcular.
    Returns:
    Factorial
    """
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


def factorial_recursivo(n):
    """
    Calcula factorial de un numero(enfoque recursivo)
    Parameters:
    n: Numero de factorial a calcular.
    Returns:
    Factorial
    """
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo(n - 1)
