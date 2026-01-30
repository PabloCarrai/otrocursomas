# Argumentos por defecto en una funcion
print("Argumentos por defecto en una funcion")


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


resultado = saludar("Pablo", saludo="Hola Como estas?", pais="Argentina")
print(resultado)
resultado1 = saludar("Yesica")
print(resultado1)
