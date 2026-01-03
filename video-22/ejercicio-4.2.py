#   Mostrar en pantalla la fecha y hora actuales del sistema.
import datetime

ahora = datetime.datetime.now()
print(f"Fecha y hora actual: {ahora}")

print(type(ahora))

ahora_formato = ahora.strftime("%H:%M:%S %Y-%M-%d")
print(ahora_formato)
