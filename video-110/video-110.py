#   Encontrar las palabras de una lista que tienen al menos 5 caracteres de longitud
palabras = [
    "SuperLocura",
    "Si",
    "Ambiguo",
    "Salame",
    "Est",
    "Sabemos",
    "Cumple",
    "Nada",
    "Aun",
]
palabras_encontradas = []
for palabra in palabras:
    if len(palabra) >= 5:
        palabras_encontradas.append(palabra)

print(f"El listado original es {palabras}")
print(f"Las palabras de al menos 5 caracteres son {palabras_encontradas}")
for palabra in palabras_encontradas:
    print(f"Palabra {palabra} con Caracteres {len(palabra)}  ")
