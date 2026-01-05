computador = {
    "id": 1001,
    "marca": "MSi",
    "ram": 128,
    "cpu": "i386",
    "almacenamiento": 8,
}

print(f"ID: {computador['id']}")  # Accedes al valor de la key id
print(f"Marca: {computador['marca']}")
print(f"Ram: {computador['ram']} GB")
print(f"CPU: {computador['cpu']}")
print(f"Almacenamiento: {computador['almacenamiento']} GB")
print(f"La variable computador tiene tantas propiedades {len(computador)} propiedades")


#   Modificacion de un diccionario
computador["marca"] = "Alien Ware"  # Asigna nuevo valor a la key marca
computador["id"] = "2001"
computador["gpu"] = "NVIDIA GeForce RTX 2080 8GB"


print(f"ID: {computador['id']}")  # Accedes al valor de la key id
print(f"Marca: {computador['marca']}")
print(f"Ram: {computador['ram']} GB")
print(f"CPU: {computador['cpu']}")
print(f"Almacenamiento: {computador['almacenamiento']} GB")
print(f"GPU: {computador['gpu']}")
print(f"La variable computador tiene tantas propiedades {len(computador)} propiedades")
