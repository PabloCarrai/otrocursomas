#   Funcion map
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def cuadrado(lista):
    cuadradros = []
    for n in lista:
        cuadradros.append(n**2)
    return cuadradros


resultado = cuadrado(numeros)
print(f"numeros tenia {numeros}")
print(f"al cuadrado es {resultado}")
#   con lista de comprension
resultado1 = [n**2 for n in numeros]
print(f"al cuadrado es {resultado1}")
resultado_lambda = list(map(lambda n: n**2, numeros))
print(f"al cuadrado es {resultado_lambda}")
