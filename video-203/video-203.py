numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = [numeros[n] for n in range(len(numeros)) if numeros[n] % 2 == 0]
sumaPares = sum(total)

print("------------------------------------------------")
print(f"Numeros tiene {numeros}")
print("------------------------------------------------")
print(f"Contenido de total {total}")
print("------------------------------------------------")
print(f"Tipo de dato de la variable total {type(total).__name__}")
print("------------------------------------------------")
print(f"Sumarizan {sumaPares}")
print("------------------------------------------------")


total1 = [numeros[n] for n in range(len(numeros)) if numeros[n] % 2 == 1]
sumaImPares = sum(total1)

print("------------------------------------------------")
print(f"Numeros tiene {numeros}")
print("------------------------------------------------")
print(f"Contenido de total1 {total1}")
print("------------------------------------------------")
print(f"Tipo de dato de la variable total1 {type(total1).__name__}")
print("------------------------------------------------")
print(f"Sumarizan {sumaImPares}")
print("------------------------------------------------")
