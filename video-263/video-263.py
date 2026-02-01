#   Crear una funcion para invertir el contenido de una cadena de caracteres


def invertirCadena(cadena):
    """
    Invierte un string pasado como argumento invertirCadena

    :param cadena: Es el string a invertir, tiene que ser str porque sino falla
    Returns:
    Devuelve la cadena invertida
    """
    if isinstance(cadena, (str)):
        return cadena[::-1]
    else:
        raise ValueError("El argumento tiene que ser una cadena(str())")


try:
    cadena = input("Ingrese una cadena para invertir   ")
    resultado = invertirCadena(cadena)
    print(f"Original --- {cadena}")
    print(f"Invertido --- {resultado}")
except ValueError as e:
    print(f"Error {e}")


#   Ahora sacando el error

try:
    cadena1 = (1, "2", 3)
    resultado1 = invertirCadena(cadena1)
    print(f"Original --- {cadena1}")
    print(f"Invertido --- {resultado1}")
except ValueError as e:
    print(f"Error {e}")
