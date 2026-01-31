#   Crear una funcion para obtener el mayor de tres numeros


def obtener_Mayor(a, b, c):
    """
    Devuelve el numero mayor entre tres valores obtener_Mayor

    :param a: Primer valor
    :param b: Segundo valor
    :param c: Tercer valor
    :return devuelve el valor mayor de tres numeros
    """

    mayor = 0
    if a > b and a > c:
        mayor = a
    elif b > a and b > c:
        mayor = b
    elif c > a and c > b:
        mayor = c
    else:
        mayor = "Hay valores iguales"
    return mayor


print(f"El mayor de los valores 2,4,55 es {obtener_Mayor(2, 4, 55)}")
