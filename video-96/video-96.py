arco_iris = {"Rojo", "Naranja", "Amarillo", "Verde", "Azul", "Añil"}
#   Operacion de subconjuntos

colores = {"Rojo", "Verde", "Azul"}
resultado = colores.issubset(
    arco_iris
)  # se fija si resultado es un subconjunto de arco_iris
print(f"El conjunto {colores} es subconjunto de {arco_iris}? {resultado}")

colores.add("Gris")  #   Agrego otro color
print(
    f"El conjunto {colores} es subconjunto de {arco_iris}? {resultado}"
)  # Porque gris no esta en arco_iris. Tienen que ser todos los elementos

vacio = set([])  # Si esta vacio no es un set(conjunto) sino un diccionario
print(f"Cantidad de elementos del conjunto vacio: {len(vacio)}")
resultado = vacio.issubset(arco_iris)  # Al estar vacio es un subconjunto
print(f"El conjunto {vacio} es subconjunto de {arco_iris}? {resultado}")
