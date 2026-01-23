#   Validar si tres valores numericos pueden pertenecer al esquema de colores RGB
def validarNumeroRGB(numero):
    if 0 <= numero <= 255:
        return True


numero = int(input("Ingrese un valor:  "))
numero1 = int(input("Ingrese otro valor:  "))
numero2 = int(input("Ingrese otro valor:  "))
print("Validando si los tres valores pertenecen al esquema RGB  ")
if validarNumeroRGB(numero) and validarNumeroRGB(numero1) and validarNumeroRGB(numero2):
    print(f"El valor {numero},{numero1},{numero2} puede pertenecer al esquema RGB")
else:
    print(f"El valor {numero},{numero1},{numero2} no puede pertenecer al esquema RGB")
