numeros = [2, 4, 6, 8, 10]
print(f"Tipo de datos de la variable numeros: {type(numeros)}")
print(f"Cantidad de elementos de la variable numeros: {len(numeros)}")
print(f"Contenido: {numeros}")
#   Acceder a sus elementos
dos = numeros[0]  #   Accedemos al primer elemento de numeros
print(f"Contenido: {dos}")
diez = numeros[4]  #   Accedemos al ultimo elemento de numeros
print(f"Contenido: {diez}")
diez = numeros[-1]  #   Accedemos al ultimo elemento de numeros
print(f"Contenido: {diez} usando indices negativos")

#   Rebanadas (slices)
subseccion = numeros[1:4]
print(f"Tipo de datos de la variable subseccion: {type(subseccion)}")
print(f"Cantidad de elementos de la variable subseccion: {len(subseccion)}")
print(f"Contenido de la variable subseccion: {subseccion}")
# desenpaquetamiento para acceder a elementos de una lista.
cuatro, seis, ocho = subseccion
print(cuatro, seis, ocho)
# antes de modificar tiene
print(f"Elementos de la variable numeros: {numeros}")
# modificar una lista
numeros[0] = 1  # cambiamos de numeros el primer valor por el valor 1
print(f"Elementos de la variable numeros: {numeros}")
