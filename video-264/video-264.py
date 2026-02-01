#   A traves de una funcion validar si un numero se halla en un rango
def valorRango(valor, rango):
    """
    Comprueba si un valor dado se halla en un rango especifico.

    :param valor: Valor a Verificar
    :param rango: Rango de valores

    Returns:
    True: si el valor se halla en el rango, False en caso contrario
    """
    if isinstance(valor, (int, float)):
        if isinstance(rango, (list, tuple)):
            if len(rango) != 2:
                raise Exception("El rango tiene que tener al menos dos elementos")
            else:
                inicio = rango[0]
                final = rango[1]
                if inicio < final:
                    if valor in range(inicio, final):
                        return True
                    else:
                        return False
                else:
                    raise ValueError(
                        "En el Rango el primer valor tiene que ser menor al segundo valor"
                    )
        else:
            raise TypeError(
                "Ha especificado un tipo valor invalido para el argumento rango, debe ser lista o tupla"
            )
    else:
        raise TypeError(
            "Ha especificado un tipo valor invalido para el argumento valor, debe ser un entero o real"
        )


try:
    rango = (1, 23)
    resultado = valorRango(2, rango)
    print(f"El valor 2 se encuentra en el rango {resultado}")
except Exception as e:
    print(f"Error {e}")

#   Ahora con lista, pero con el inicio mayor al final
try:
    rango1 = [100, 23]
    resultado1 = valorRango(233, rango1)
    print(f"El valor 233 se encuentra en el rango {resultado1}")
except Exception as e:
    print(f"Error {e}")
