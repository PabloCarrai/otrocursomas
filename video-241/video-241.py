def sumar(numero1, numero2):
    """
    Suma dos numeros(sean enteros o puntos flotantes)

    Parameters:
    numero1:primer valor a sumar.
    numero2:segundo valor a sumar.

    Returns:
    suma de dos numeros(enteros o reales).
    """
    suma = numero1 + numero2
    return suma


# invocacion de la funcion
x = 2
y = 3
resultado = sumar(x, y)  # invocacion de la funcion sumar
print(f"El resultado de sumar {x} y {y} es {resultado}")

# otra forma de invocacion es
resultado = sumar(2, 3)
print(f"El resultado de sumar es {resultado}")


#   obtener documentacion ayuda de una funcion
help(sumar)  # nos muestra info sobre la funcion
print()
#help(print)
