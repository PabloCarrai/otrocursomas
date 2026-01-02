nombre = "Romina"  # Cadena de caracteres
apellido = "Nomeacuerdo"
nombre_completo = nombre + " " + apellido  # con + concatenamos dos caracteres

print("Nombre: ", nombre)
print("Apellido: ", apellido)
print("Nombre Completo: ", nombre_completo)

print()
print("Tipo de datos de la variable nombre: ", type(nombre))
print("Tipo de datos de la variable apellido: ", type(apellido))
print("Tipo de datos de la variable nombre_completo: ", type(nombre_completo))

print()
edad = 29
resultado = nombre_completo + " tiene " + str(edad) + " años."
print(resultado)
print()
resultado = "{} tiene {} años".format(nombre_completo, edad)
print(resultado)