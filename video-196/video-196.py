#   Ciclos  for
#   Recorre colecciones que tienen un numero de elementos fijos

numeros = [1, 2, 3, 4, 5]
total = 0

#   Metodo sin for
total = numeros[0] + numeros[1] + numeros[2] + numeros[3] + numeros[4]
print(f"El total Suma {total}")
print("-----------------------------------------------------")

#   Otro Metodo sin for
total1 = 0
total1 += numeros[0]
total1 += numeros[1]
total1 += numeros[2]
total1 += numeros[3]
total1 += numeros[4]
print(f"El total Suma {total1}")
print("-----------------------------------------------------")
