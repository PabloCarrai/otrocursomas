numero = int(input("Ingrese un numero entero:  "))
if (
    numero % 5 == 0
    and 20 <= numero <= 40  #    Es lo mismo a estar entre los dos valores
):  #    con and puedo poner mas de una condicion a probar
    print(
        f"El numero {numero} es divisible entre 5 y se halla en el rango entre 20 y 40"
    )
else:
    print(
        f"El numero {numero} no es divisible por 5 y no se encuentra entre el rango 20 y 40"
    )
