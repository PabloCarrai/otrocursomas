# Terminacion arbitraria de un ciclo while
total = 0
# Ciclo infinito
while True:
    numero = int(input("Numero entero? (negativo para finaliza) "))
    if numero <= 0:  #   Esta es la condicion para salir del while
        break  #   Esto sale del bucle
    else:
        total += numero

print(f"El total es {total}")
