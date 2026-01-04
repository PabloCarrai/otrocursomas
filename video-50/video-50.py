#   Uso del metodo split()
valores = "2,3,5,7,11"
valores_separados = valores.split(",")
print(len(valores))
print(valores)
print(valores_separados)
print(type(valores_separados[0]))
#   Uso del metodo str.find()
indice = valores.find("2")
print(f"El indice del elemento 2 es igual a {indice}")

indice = valores.find("1")
print(
    f"El indice del elemento 1 es igual a {indice}"
)  # Muestra el indice de la primer ocurrencia del elemento

indice = valores.find("8")
print(
    f"El indice del elemento 8 es igual a {indice}"
)  #    -1 es que el elemento no se encontro
