#   Calcular el area superficial y el volumen de un cilindro
#   Area superficial
from math import pi

radio = float(input("Ingrese el radio del cilindro   "))
altura = float(input("Ingrese la altura del cilindro   "))
areaSuperficial = (2 * pi * radio**2) + (2 * pi * radio * altura)
volumenCilindro = pi * radio**2 * altura
print("-----------------------------------------")
print(f"El area del cilindro es : {areaSuperficial}   ")
print("-----------------------------------------")
print(f"El volumen del cilindro es : {volumenCilindro}   ")
print("-----------------------------------------")
