edad = 45
dias_vividos = edad * 365
print(edad)
print(dias_vividos)

print(
    "Tipos de datos de la variable edad: ", type(edad)
)  #   muestra el tipo de datos contiene la variable edad
print("Tipos de datos de la variable dias_vividos: ", type(dias_vividos))


print()
print(
    "Posicion en memoria de la variable edad:", id(edad)
)  #   Devuelve posicion en memoria de la variable dia
print("Posicion en memoria de la variable dias_vividos:", id(dias_vividos))
print()
print("Posicion en memoria de la variable 45:", id(45))
print("Posicion en memoria de la variable 16425:", id(16425))
