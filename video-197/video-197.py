#   Ciclos for
numeros = [1, 2, 3, 4, 5]
numeros.append(6)
numeros.append(7)
numeros.append(8)
numeros.append(9)
numeros.append(10)
print(f"Contenido actual de numeros {numeros}")
total1 = 0
total1 += numeros[0]
total1 += numeros[1]
total1 += numeros[2]
total1 += numeros[3]
total1 += numeros[4]
total1 += numeros[5]
total1 += numeros[6]
total1 += numeros[7]
total1 += numeros[8]
total1 += numeros[9]
print(f"La suma de numeros {total1}")
#   Uso explicito de for para resolver esto.
total1 = 0
for i in range(
    0, len(numeros)
):  
    total1 += numeros[i]  #   Sumo a total1 numeros en la posicion i
print(f"La suma de numeros {total1}")