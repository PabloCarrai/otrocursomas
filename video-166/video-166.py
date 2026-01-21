#   Convertir Radianes a Grados
# grados=radianes * 180/pi
from math import pi

radianes = float(input("Ingrese los radianes   "))
grados = radianes * (180 / pi)
print("-----------------------------------------")
print(f"Resultado {grados} Grados  ")
print("-----------------------------------------")
