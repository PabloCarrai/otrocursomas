#   Pedir al usuario que adivine un numero. Solo un intento
from random import randint as rd

valorAleatorio = rd(1, 10)
valorElegido = int(input("Adivina un numero del 1 al 10  "))
if valorAleatorio == valorElegido:
    print(
        f"El numero elegido es {valorAleatorio} y tu elegistes {valorElegido} has acertado"
    )
else:
    print(
        f"El numero elegido es {valorAleatorio} y tu elegistes {valorElegido} no acertaste"
    )

