#   Operador logico O(or)
#   Con que una sola de las condiciones de true esto termina siendo True
print("Operador logico O(or)")
edad = 23
profesion = "Programador"
califica = edad > 20 or profesion == "Programador"
print(f"La persona tiene mas de 20 años o es programadora ? {califica}")
edad = 17
profesion = "Ingeniero"
califica = edad > 20 or profesion == "Programador"
print(f"La persona tiene mas de 20 años o es programadora ? {califica}")
