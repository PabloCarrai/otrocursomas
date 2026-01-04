#   Inmutabilidad en tuplas(no se puede cambiar el contenido de la tupla)

punto = (2, 5)

# punto[0] = 3  #   No se puede porque no soporta asignacion(no es mutable)
# punto[1] = 7    #   No se puede porque no soporta asignacion(no es mutable)
#   Recreando una tupla
punto=(3, 7)  # Esto ya es otra tupla(se rescribe la original y es otra)
x = punto[0]
y = punto[1]
print(f"El valor en x es igual a: {x}")
print(f"El valor en y es igual a: {y}")