#   Argumentos nombrados variables:
print("#   Argumentos nombrados variables:")


#   Se trabaja como un diccionario
def mostrar_identidad(**identificacion):
    resultado = ""
    if identificacion.get("documento"):
        resultado += "Documento: " + identificacion.get("documento")
    if identificacion.get("nombre"):
        resultado += "Nombre: " + identificacion.get("nombre")
    if identificacion.get("apellido"):
        resultado += "Apellido: " + identificacion.get("apellido")

    return resultado


persona = mostrar_identidad(nombre="Pablo ", apellido="Ortiz ")
print(f"Identificacion: {persona}")

persona = mostrar_identidad(documento="28406166 ", nombre="Pablo ", apellido="Ortiz ")
print(f"Identificacion: {persona}")
