#   Solicitar al usuario una cantidad arbitraria de numeros y luego
#   calcular su suma y producto
valores = []
cvalores = int(input("Cuantos valores ingresaras?  "))
for valor in range(cvalores):
    numero = int(input("Valor?  "))
    valores.append(numero)

suma = 0
producto = 1
for v in valores:
    suma += v
for p in valores:
    producto *= p

print(f"Los valores son {valores}")
print(f"La suma da {suma}")
print(f"El producto da {producto}")
