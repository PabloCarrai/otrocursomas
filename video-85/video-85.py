computador = {
    "id": 1001,
    "marca": "MSi",
    "ram": 128,
    "cpu": "i386",
    "almacenamiento": 8,
}

#   popitem() sobre diccionarios   # extra un llave valor de un diccionario
print(computador)
atributo = computador.popitem()
print(computador)
print(atributo)
print(type(atributo))
print(f"llave: {atributo[0]} valor: {atributo[1]}")
