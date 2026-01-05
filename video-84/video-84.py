computador = {
    "id": 1001,
    "marca": "MSi",
    "ram": 128,
    "cpu": "i386",
    "almacenamiento": 8,
}


# netodo pop()  elimina un elemento del diccionario devuelve KeyError: por no existir
print(
    computador.pop("almacenamiento")
)  #   Si existe devuelve el valor pero elimina llave y valor
valor = computador.pop("marca")
print(f"Se ha removido la llave marca de computador {valor}")
print("marca" in computador)
