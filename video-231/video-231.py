versiones = {"Python": "3.8.1", "Java": "12", "JavaScript": "ES6", "C#": "8"}
lenguaje = input("Escriba un nombre de lenguaje de programacion   ")
try:
    version = versiones[lenguaje]
    print(f"La version de {lenguaje} es {version}")
except KeyError as err:
    print(f"Error {err}")
print("Fin del programa")

#   sobreescribe cuando la llave no existe
version = versiones.get("java", "1.0.0")  # devuelve none si la llave no existe
print(f"La version de {lenguaje} es {version}")
