#   Con lambda

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = list(filter(lambda n: n % 2 != 0, numeros))

print(f"Impares con lista de comprension {resultado}")
print(f"Cantidad elementos impares {len(resultado)}")


def filtro(n):
    return n % 2 != 0


resultado1 = list(filter(filtro, numeros))
print(f"Impares con lista de comprension {resultado1}")
print(f"Cantidad elementos impares {len(resultado1)}")
