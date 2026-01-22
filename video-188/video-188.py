#   Dada la recta y=6x +10, comprobar si un punto
#   dato pertenece a ella.
x = float(input("Escriba el valor de x:  "))
y = float(input("Escriba el valor de y:  "))
valor = 6 * x + 10
if valor == y:
    print(f"El punto( {x}, {y} ) se halla en la recta y=6x+10")
else:
    print(f"El punto( {x}, {y} ) no se halla en la recta y=6x+10")