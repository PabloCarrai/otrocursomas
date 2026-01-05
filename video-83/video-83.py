computador = {
    "id": 1001,
    "marca": "MSi",
    "ram": 128,
    "cpu": "i386",
    "almacenamiento": 8,
}

#   Metodos y operadores de diccionarios
# convertir llaves de un diccionario a una lista
atributos = list(computador)
print(atributos)
print(f"Cantidad de llaves del diccionario {len(atributos)}")
print(type(atributos))
#   Operador in en diccionario
print("board" in computador)  # se fija si board se encuentra en computador
print("ram" in computador)