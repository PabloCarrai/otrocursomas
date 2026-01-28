#   Errores al acceder a un atributo inexistente de una clase
class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio


computador = Producto(1001, "Computador", 799)
print(f"Codigo {computador.codigo}")
print(f"Nombre: {computador.nombre}")
print(f"Precio: {computador.precio}")

try:
    print(f"Cantidad: {computador.cantidad}")  #   No existe ese atributo
except AttributeError as err:
    print(f"Error {err}")
    print("Esta tratando de acceder a un atributo inexistente")
