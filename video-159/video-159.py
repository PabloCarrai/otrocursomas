resultado = 13 + 3 ** (1 / 2)  #   Esta mal por la precedencia de la potencia
print(f"El contenido de resultado es {resultado}")
print("------------------------------------------")
# Asi esta bien el anterior da mal
resultado = (13 + 3) ** (1 / 2)
print(f"El contenido de resultado es {resultado}")
print("------------------------------------------")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado1 = sum(numeros[:5])  # Suma solo hasta el quinto elemento
print(f"El contenido de resultado1 es {resultado1}")
