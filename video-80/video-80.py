#   Iteracion en diccionario
computador = {
    "id": 1001,
    "marca": "MSi",
    "ram": 128,
    "cpu": "i386",
    "almacenamiento": 8,
}

print("Iteracion en diccionarios ")
for k in computador.keys():  #   Solo iteramos las llaves(keys)
    print(k)

for k in computador.keys():  #   Ahora vemos llave y valor
    print(f"{k.upper()}: {computador[k]}")
