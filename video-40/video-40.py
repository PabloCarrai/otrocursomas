llueve = False
print(type(llueve))
print(llueve)
if llueve:
    print("El dia esta lluvioso")
else:
    print("El dia esta esplendido")
llueve = not llueve
print(llueve)
if llueve:
    print("El dia esta lluvioso")
else:
    print("El dia esta esplendido")
print()
# operaciones con booleanos(logicos)
a = True
b = False
#   operadores logicos and(conjuncion-y) or (disyuncion-o)
print(a and b)  #   Devuelve False porque una de las dos es false
print(a and not b)  # devuelve true porque ambas son true
print(b or a)  # una de las dos se cumple, asi que devuelve true
print(b or not a)  # false porque negamos una verdad en a
