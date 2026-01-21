#   Calcular el area de un trapezoide
# area=((BaseMayor+baseMenor)*altura)/2

baseMayor = float(input("Ingresa la Base Mayor:  "))
baseMenor = float(input("Ingresa la Base Menor:  "))
altura = float(input("Ingresa la Altura:   "))
area = ((baseMayor + baseMenor) * altura) / 2
print("-----------------------------------------")
print(f"El area del trapezoide es: {area}   ")
print("-----------------------------------------")
