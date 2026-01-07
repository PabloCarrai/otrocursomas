#   Convertir un diccionario en su representacion en el formato json
import json
diccionario = {"Nombre": "Paula", "Edad": 35, "Estudios": "Secundario"}
cadena_json = json.dumps(diccionario)
print(f"El diccionario es {diccionario}")
print(f"Su tipo es {type(diccionario)}")
print(f"Convertido a json es {cadena_json}")
print(f"Su tipo es {type(cadena_json)}")
