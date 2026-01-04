#   booleano
#   Falso = False Verdadero = True
llueve = False
print(type(llueve))
print(llueve)
if llueve:
    print("El dia esta lluvioso")
else:
    print("El dia esta esplendido")
llueve = not llueve  # Niega el valor
print(llueve)
if llueve:
    print("El dia esta lluvioso")
else:
    print("El dia esta esplendido")
