#   Generar los primeros 50 numeros de la serie fibonacci

numero1, numero2 = 0, 1
for _ in range(50):
    print(numero1, end=",")
    numero1, numero2 = numero2, numero1 + numero2
