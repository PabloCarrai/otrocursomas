punto = (2, 5)
print(f"Tipo de datos {type(punto)}")
print(f"Contenido de la variable punto:  {punto}")
print(f"Cantidad de elementos de la tupla punto: {len(punto)}")
#   Acceso a los elementos de una tupla
x = punto[0]
y = punto[1]
print(f"El valor en x es igual a: {x}")
print(f"El valor en y es igual a: {y}")
#   Desenpaquetamiento
abscisa, ordenada = punto
print(f"El valor en abscisa es igual a: {abscisa}")
print(f"El valor en ordenada es igual a: {ordenada}")
#   Acceder al ultimo elemento usando elementos negativos(de derecha a izquierda)
penultimo_elemento = punto[-2]
ultimo_elementos = punto[-1]
print(f"El valor en penultimo_elemento es igual a: {penultimo_elemento}")
print(f"El valor en ultimo_elementos es igual a: {ultimo_elementos}")

