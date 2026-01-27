# excepciones aritmetica

while True:
    try:
        dividendo = float(input("Escriba el dividendo "))
        break
    except:
        print("Debe escribir un valor valido")

while True:
    try:
        divisor = float(input("Escriba el divisor "))
        break
    except:
        print("Debe escribir un valor valido")

try:
    division = dividendo / divisor
    print(f"El resultado de la division es {division}")
except ZeroDivisionError as err:
    print(f"Error {err}")
    print("Intento de division sobre cero")
