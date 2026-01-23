#   Dadas la rectas y=2x-2, y y=x+1,x=10 comprobar si un punto
#   esta en el area comprendida entre las rectas.
x = float(input("Ingrese valor de x: "))
y = float(input("Ingrese valor de y: "))

if x <= 10:
    valor_1 = 2 * x - 2
    valor_2 = x + 1
    if valor_2 <= y <= valor_1:
        print(f"El punto ( {x},{y} ) se halla en el area de las tres rectas")
    else:
        print(f"El punto ( {x},{y} ) no se halla en el area de las tres rectas")
else:
    print(f"El punto ( {x},{y} ) no se halla en el area de las tres rectas")
