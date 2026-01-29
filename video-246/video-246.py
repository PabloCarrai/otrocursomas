#   Lista variable de argumento de una funcion
print("#   Lista variable de argumento de una funcion")


# def sumar(a, b):
#     return a + b


# def sumartres(a, b, c):
#     return a + b + c


# def sumarcuatro(a, b, c, d):
#     return a + b + c + d


# *valores es una cantidad de variable de argumentos
def sumar(*valores):
    suma = 0
    for valor in valores:
        suma += valor
    return suma


resultado = sumar(1, 2)
print(f"El valor de resultado es {resultado}")
resultado = sumar(1, 2, 2)
print(f"El valor de resultado es {resultado}")
resultado = sumar(1, 2, 3, 4, 5)
print(f"El valor de resultado es {resultado}")
