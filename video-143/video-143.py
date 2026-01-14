#   Operadores logico Y(and)
print("Operador logico Y(and)")
edad = 19
nombre = "Daniela"
# para ser true tiene que cumplirse ambas
resultado = (edad >= 18) and (nombre == "Daniela")
print(f"La persona se llama Daniela y es mayor de edad {resultado}")
edad = 17
resultado = (edad >= 18) and (nombre == "Daniela")
print(f"La persona se llama Daniela y es mayor de edad {resultado}")
