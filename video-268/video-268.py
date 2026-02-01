#   Crear una funcion recursiva para comprobar si una cadena es palindromo
def es_palindromo(palabra):
    """
    Determina si una palabra es palindromo

    :param palabra: Palabra a la que se le realiza la comprobacion
    Returns:
    true en caso afirmativo false caso contrario
    """
    if isinstance(palabra, str):
        if len(palabra) < 1:
            return True
        else:
            if palabra[0] == palabra[-1]:
                return es_palindromo(palabra[1:-1])
            else:
                return False
    else:
        raise ValueError("Se requiere un argumento que sea cadena(str)")


print(f"oso es palindromo? {es_palindromo("oso")}")
print(f"carniceria es palindromo? {es_palindromo("carniceria")}")
try:
    print(f"oso es palindromo? {es_palindromo(2)}")
except ValueError as e:
    print(f"Error {e}")
