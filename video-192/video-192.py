#   Determinar si un numero dado por el usuario es par o impar
numero = int(input("Ingresa un numero  "))
if numero % 2 == 0:
    print(f"El numero {numero} es par")
else:
    if numero % 2 != 0:
        print(f"El numero {numero} es impar")
