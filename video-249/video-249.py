def saludar(nombre, saludo="Hola", pais="Colombia"):
    """
    Saluda utilizando un saludo, un nombre y un pais de procedencia

    :param nombre: nombre de a quien saluda
    :param saludo: mensaje del saludo
    :param pais: pais de procedencia
    :returns: frase con el saludo que incluye las otras variables
    """
    frase = f"{saludo}, mi nombre es {nombre}, soy de {pais}"
    return frase


resultado = saludar("Olive", pais="España", saludo="Buenas noches")
print(f"Resultado: {resultado}")


def exponenciacion(base, exponente=2):
    """
    Calcula la exponenciacion de un numero base respecto a un exponente

    :param base: Base de la exponenciacion
    :param exponente: Exponente(potencia de la exponenciacion valor por defecto 2)
    :returns: exponenciacion de una base y un exponente
    """
    resultado = base**exponente
    return resultado


potencia = exponenciacion(5)
print(f"Resultado: {potencia}")
potencia1 = exponenciacion(10, 3)
print(f"Resultado: {potencia1}")
