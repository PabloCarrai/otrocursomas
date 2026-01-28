#   Creacion de una funcion para alternar los valores de dos variables

print("Creacion de una funcion para alternar los valores de dos variables")


def alternarValores(valor1, valor2):
    """
    Pide dos valores en variables e intercambia dichos valores devolviendolo en en forma de tupla

    Parameters:
    valor1:primer valor a sumar.
    valor2:segundo valor a sumar.

    Se usa un auxiliar para el intercambio de valores

    Returns:
    devuelvo de dos valores(enteros o reales) intercambiados en orden en forma de tupla.
    """
    auxiliar = valor1
    valor1 = valor2
    valor2 = auxiliar

    return (valor1, valor2)


resultado = alternarValores(32, 211)
# print(help(alternarValores))
print(resultado)

x = 19
z = 22
resultado1 = alternarValores(x, z)
print(f"Pasamos x:{x} e y:{z} y obtuvimos {resultado1}")
