#   Generar una funcion recursiva para dividir dos numeros


def dividir(dividendo, divisor):
    """
    Calcula la division de 2 numeros

    :param dividendo: Dividendo de la division
    :param divisor: Divisor de la division
    Returns:
    Division entre dividendo y divisor
    """
    if divisor == 0:
        raise ZeroDivisionError("El divisor no puede ser 0")
    elif dividendo == divisor:
        return 1
    elif dividendo < divisor:
        return 0
    else:
        return 1 + dividir(dividendo - divisor, divisor)


print(f"La division entre {5} / {2} es {dividir(5,2)}")
print(f"La division entre {1} / {2} es {dividir(1,2)}")
try:
    print(f"La division entre {1} / {0} es {dividir(1,0)}")
except ZeroDivisionError as e:
    print(f"Error {e}")
