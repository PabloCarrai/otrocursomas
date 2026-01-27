#   Excepciones acceso a elementos de una lista
nombres = ["python", "c++", "c", "javascript", "go", "ruby"]
print(f"Cantidad de elementos de la lista nombres {len(nombres)}")
print(f"Elementos de la lista nombre {nombres}")
print(f"Primer elemento {nombres[0]}")

indice = 6
try:
    print(f"Ultimo elemento {nombres[indice]}")
except IndexError:
    print(f"El indice {indice} no existe en nombres")

#   Acceso a ultimo elemento con Indices negativos
print(f"Ultimo elemento de nombres {nombres[-1]}")
indice = -7
try:
    nombres = nombres[nombres]
    print(f"Primer elemento de nombres {nombres}")
except:
    print(f"El indice {indice} no existe en nombres")
