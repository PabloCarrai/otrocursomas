#   Capturar una palabra o frase del usuario e invertirla
frase = input("Ingresa una palabra o frase  ")
print(f"La frase original: {frase}")
frase_invertida = ""
for i in range(len(frase) - 1, -1, -1):
    frase_invertida = frase_invertida + frase[i]
print(f"La frase resultante: {frase_invertida}")

otra_Frase_invertida=frase[::-1]
print(f"La frase resultante: {otra_Frase_invertida}")
