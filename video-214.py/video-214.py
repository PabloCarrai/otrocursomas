#   Calcular el factorial de un numero dado por el usuario
numero = int(input("Ingrese un numero: "))
factorial = 1

if numero <= 0:
    print("Factorial no esta definido para negativos")
else:
    for i in range(1, numero + 1):
        factorial *= i

print(f"Factorial de {numero} es {factorial}")
