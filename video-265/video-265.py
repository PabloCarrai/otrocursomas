#   Usar una funcion para contar minusculas y mayusculas en una cadena.


def contarMayusculasMinusculas(frase):
    """
    Devuelve una tupla con el valor de la cantidad de minusculas y mayusculas en una frase

    :param frase: Es el string a revisar
    Returns:
    Tupla con la cantidad de minusculas y mayusculas
    """
    if isinstance(frase, (str)):
        minusculas_contador = 0
        mayusculas_contador = 0
        for letra in frase:
            if letra.isupper():
                mayusculas_contador += 1
            else:
                minusculas_contador += 1
        return (minusculas_contador, mayusculas_contador)
    else:
        raise TypeError("El argumento tiene que ser una cadena(str())")


prueba = "SuperCalifrasquiListicoEspiadidoso"
print(f"Original {prueba}")
try:
    minusculas, mayusculas = contarMayusculasMinusculas(prueba)
    print(f"Minusculas: {minusculas}")
    print(f"Mayusculas: {mayusculas}")
except TypeError as e:
    print(f"Error {e}")


#   Viendo que no envio un string

prueba1 = ("SuperCalifrasquiListicoEspiadidoso", "Locura")
print(f"Original {prueba1}")
try:
    minusculas1, mayusculas1 = contarMayusculasMinusculas(prueba1)
    print(f"Minusculas: {minusculas1}")
    print(f"Mayusculas: {mayusculas1}")
except TypeError as e:
    print(f"Error {e}")
