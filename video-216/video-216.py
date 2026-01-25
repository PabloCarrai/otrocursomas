#   Encontrar todos los numeros pares que hay en el rango de 100 a 400

for numero in range(100, 401):
    if numero % 2 == 0:
        print(f"Numero par {numero}")
