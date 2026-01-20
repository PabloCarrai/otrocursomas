#   Linealizacion de expresiones albegraicas a expresiones programaticas.
#   Linealizar ecuacion cuadratica

a = 1
b = 0
c = -1


x_1 = (-b + (b**2 - 4 * a * c) ** (1 / 2)) / (2 * a)
x_2 = (-b - (b**2 - 4 * a * c) ** (1 / 2)) / (2 * a)
print("---------------------------------------------")
print(f"Solucion 1 (x_1): {x_1}")
print("---------------------------------------------")
print(f"Solucion 2 (x_2): {x_2}")
