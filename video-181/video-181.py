#   Realizar aumento sobre los ahorro dependiendo de la cantidad ahorrada
ahorro = float(input("Ingrese el monto ahorrado actualmente:  "))
if ahorro > 0:
    if ahorro < 1000000:
        ahorro *= 1.10
    elif ahorro < 3000000:
        ahorro *= 1.07
    elif ahorro < 10000000:
        ahorro = ahorro * 1.05
    else:
        ahorro *= 1.03
    print(f"El ahorro se ha incrementado a ${ahorro}")
else:
    print(f"Usted ha digitado una cantidad negativa o igual a cero")

print("El programa ha finalizado")
