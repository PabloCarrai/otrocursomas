#   Sumar todos los valores de un diccionario
producto = {
    "Mouse": 29.9,
    "Teclado": 119.9,
    "Audifonos": 35.9,
    "Monitor": 299,
}

contador = 0
for valor in producto.values():
    contador += valor
print(f"El diccionario {producto} sumariza un valor de {contador}")
