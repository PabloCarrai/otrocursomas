arco_iris = {"Rojo", "Naranja", "Amarillo", "Verde", "Azul", "Añil"}
colores = {"Rojo", "Verde", "Azul"}
#   Operacion de superconjunto (elementos del primer conjunto incluye todo del otro conjunto)
rgb = {"Verde", "Azul", "Rojo"}
resultado = arco_iris.issuperset(rgb)
print(f"¿El conjunto {arco_iris} es superconjunto de {rgb}? {resultado}")

rgb.add("Gris")
print(f"¿El conjunto {arco_iris} es superconjunto de {rgb}? {resultado}")
