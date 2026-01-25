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
print(f"-----------------------------------------------")
total1 = 0
#   Suma de los pares en numeros
sumaPar = 0
for i in range(len(numeros)):  # se puede omitir el indice de inicio
    if numeros[i] % 2 == 0:  # Reviso si numeros en la posicio i modulo 2 da 0
        sumaPar += numeros[i]  #  Lo sumo
print(f"La suma de los pares es {sumaPar}")
