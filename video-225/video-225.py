print("Captura de un numero entero  ")
while True:
    try:
        edad = int(input("Edad? "))
        if edad > 0:
            break
        else:
            print("El valor de edad tiene que ser numero positivo")
    except:
        print("No escribio un valor valido, intente nuevamente")

print(f"Su edad es {edad}")
