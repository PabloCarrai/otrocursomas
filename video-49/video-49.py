lenguaje = "Python"

# lenguaje[0] = ("p")  Los elementos str no soportan asignacion de elemento(no se pueden modificar)


#   Inmutables, se dicen son estaticos
print(id("Python") == id("Python"))

print(lenguaje)
lenguaje = (
    "Python".lower()
)  # convierte los caracteres en minuscula, pero haciendo una copia de esos str y sobreescribiendo la variable
print(lenguaje)
