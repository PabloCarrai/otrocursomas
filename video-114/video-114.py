# remover los elementos duplicados de un diccionario
productos = {
    1001: "Mouse",
    1002: "Teclado",
    1003: "Monitor",
    1004: "Mouse",
    1005: "Audifonos",
    1006: "Teclado",
}
print(f"Contenido de productos {productos}")
print(f"Cantidad de productos {len(productos)}")
productos_unicos = {}

for k, v in productos.items():
    if v not in productos_unicos.values():
        productos_unicos[k] = v

print(f"Contenido de productos_unicos {productos_unicos}")
print(f"Cantidad de productos_unicos {len(productos_unicos)}")
