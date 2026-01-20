from math import sqrt  # permite calcular raices cuadradas

#   Sumamos la raiz cuadrada de 25
resultado = 5 / (2 + 4) + sqrt(25)  # Suma la raiz cuadrada de 25
print(f"El contenido de resultado es {resultado}")
print("Otra cosa(Aca esta mal)")
#   Porque primero hace la potencia y luego la division
resultado = 25**1 / 2
print(f"El contenido de resultado es {resultado}")
#   Aca esta bien
print("Asi se hace")
resultado = 25 ** (1 / 2)  # Otra forma de conseguir la raiz cuadrada de 25
print(f"El contenido de resultado es {resultado}")
