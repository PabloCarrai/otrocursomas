#   Operador is
print("Operador is")
numero1 = [1, 2, 3, 4, 5]
numero2 = numero1  #   Aca solo da true para el operador is
numero3 = [1, 2, 3, 4, 5]
numero4 = [1, 2, 3, 5, 4]
print(numero1)
print(numero2)
print(numero3)
print(numero4)
print(numero1 == numero2)
print(numero1 == numero3)
print(numero2 == numero3)
print(numero1 == numero4)
print("Operador is ")  # Compara igualdad de referencia, si es el mismo objeto
print(numero1 is numero2)
print(numero1 is numero3)
print(numero2 is numero3)
