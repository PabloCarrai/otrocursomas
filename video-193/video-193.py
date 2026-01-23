#   Comprobar si un numero es capicua


def capicua(numero):
    #   Transformo el numero en string para comparar el mismo y el reverso
    return str(numero) == str(numero)[::-1]


numero = int(input("Ingrese un numero  "))
if numero<=0:
    print("El numero es negativo, tiene que ser positivo")
else:
    if capicua(numero):
        print(f"El numero {numero} es capicua")
    else:
        print(f"El numero {numero} no es capicua")
