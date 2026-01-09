#   Operador de resto %
#   Calculamos la divisio entera entre 5 y 2

numero = 5
numero1 = 2
division = numero // numero1
resto = numero % numero1
print(
    f"La variable numero tiene {numero} y numero1 {numero1} la division da {division} y el resto {resto}"
)
print(f"Es par o impar?")
if numero % 2 == 0:
    print(f"El valor {numero} es par")
else:
    print(f"El valor {numero} es impar")
