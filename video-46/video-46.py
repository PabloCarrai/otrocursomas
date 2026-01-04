nombre = "Mirian Gomez"  #   Ejemplo
email = "mgomez@gmail.com"
direccion = """  Baigorria 2321  """

print(type(nombre))
print(nombre)

mensaje = "Bienvenido(a), " + nombre + ". Correo: " + email
print(type(mensaje))
print(mensaje)

#   Interpolacion de cadena de caracteres
mensaje = f"Bienvenido(a), {nombre}. Correo: {email}"  #   Este es mi favorito
print(mensaje)

#   metodo format de clase str
mensaje = "Bienvenido(a), {}. Correo: {}".format(nombre, email)
print(mensaje)

#   con %
mensaje = "Bienvenido(a), %s. Correo: %s" % (nombre, email)
print(mensaje)
