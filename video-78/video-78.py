computador = {
    "id": 1001,
    "marca": "MSi",
    "ram": 128,
    "cpu": "i386",
    "almacenamiento": 8,
}
#   Acceder a las propiedades
print(f"ID: {computador['id']}")  # Accedes al valor de la key id
print(f"Marca: {computador['marca']}")
print(f"Ram: {computador['ram']} GB")
print(f"CPU: {computador['cpu']}")
print(f"Almacenamiento: {computador['almacenamiento']} GB")


print(
    computador.get("Almacenamiento", "1")
)  # cuando no se encuentra Almacenamiento pone por defecto 1
