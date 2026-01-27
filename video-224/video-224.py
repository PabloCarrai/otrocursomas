#   Captura de un numero entero
print("Captura de un numero entero  ")
while True:
    try:
        edad = int(input("Edad? "))
        break
    except:
        print("No escribio un valor valido, intente nuevamente")

print(f"Su edad es {edad}")
