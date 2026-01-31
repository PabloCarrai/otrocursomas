def cuadrado(n):
    return n**2


cuadrado_lambda = lambda n: n**2
numero = 10
print(f"El cuadrado de {numero} es {cuadrado_lambda(numero)}")
print(f"El cuadrado de {numero} es {cuadrado(numero)}")
