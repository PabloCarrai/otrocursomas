#   Encontrar los tres valores mayores en un diccionario
#   Sumar todos los valores de un diccionario
from heapq import nlargest

producto = {
    "Mouse": 29.9,
    "Teclado": 119.9,
    "Audifonos": 35.9,
    "Monitor": 299,
}

productos_mas_caros_3 = nlargest(3, producto, key=producto.get)
print(f"Los 3 mas caros es {productos_mas_caros_3}")