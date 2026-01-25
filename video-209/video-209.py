# Terminacion arbitraria de un ciclo while
total = 0
# Ciclo infinito
while True:
    numero = int(input("Numero entero? (negativo para finaliza) "))
    if numero <= 0:
        break  #   Esto sale del bucle
    else:
        total += numero

print(f"El total es {total}")
