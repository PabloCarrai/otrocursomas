computador = {
    "id": 1001,
    "marca": "MSi",
    "ram": 128,
    "cpu": "i386",
    "almacenamiento": 8,
}
#   reversed()  actua sobre las llaves del diccionario
print(computador)
print(list(computador))
print(list(reversed(computador)))
print(computador)

#
print("Antes")
for k in computador:
    print(k)
print("Despues")
for k in reversed(computador):
    print(k)
