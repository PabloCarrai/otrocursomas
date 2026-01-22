#   esto es del 173, el tipo envio un amage malisimo
#   input()
try:
    nombre = input("Digite su nombre:  ")
    print(f"El tipo de dato de la variable nombre es: {type(nombre).__name__}")
    print(f"El contenido de la variable nombre es: {nombre}")
except EOFError as err:
    print(f"El usuario a cancelado la introduccion de datos {err}")
    print("El nombre de la persona no se capturo")
finally:
    print("El programa finalizo de forma correcta ")
