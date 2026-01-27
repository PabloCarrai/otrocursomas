try:
    numero = int(input("Escriba un numero entero:    "))
    print(f"La variable numero es {numero}")
    print(f"La variable numero es del tipo {type(numero).__name__}")
except ValueError as err:
    print(f"Error: {err}")

print("Programa terminado")
