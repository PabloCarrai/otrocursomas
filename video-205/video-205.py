#   Ciclo while
numeros = [1, 2, 3, 4, 5]
i = 0  # Es necesario para tener una manera de salir del while
while i < len(numeros):
    print(f"El valor de numeros en indice i es {numeros[i]}")
    i += 1  # Esto evita que sea un ciclo infinito
