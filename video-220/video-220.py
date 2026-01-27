# calcular media, minimo y maximo
valores = []
seguimos = "si"
while seguimos == "si":
    valor = int(input("Ingrese un numero  "))
    valores.append(valor)
    seguimos = input("Desea cargar otro? si para continuar no para salir  ")
total = 0
cvalores = len(valores)
for e in valores:
    total += e
media = total / cvalores
minimo = valores[0]
for x in valores:
    if x < minimo:
        minimo = x
maximo = valores[0]
for i in valores:
    if i > maximo:
        maximo = i

print(f"La media de los valores {valores} es {media}")
print(f"El minimo de valores  {valores} es {minimo} ")
print(f"El maximo de valores  {valores} es {maximo} ")
