llave_1 = True
llave_2 = False
if llave_1 and not llave_2:
    print("Si hay agua")
else:
    print("No hay agua")
if llave_1 or llave_2:
    print("Si hay agua")
else:
    print("No hay agua")
if not llave_1 or llave_2:
    print("Si hay agua")
else:
    print("No hay agua")
if llave_1 and llave_2:
    print("Si hay agua")
else:
    print("No hay agua")
print("Uso de la clase bool()")
x = bool(1)
print(type(x))
print(x)
x = bool(123)
print(type(x))
print(x)
x = bool(-123)
print(type(x))
print(x)
x = bool(0)
print(type(x))
print(x)
x = bool("False")
print(type(x))
print(x)
x = bool("True")
print(type(x))
print(x)
x = bool(123 < 124)
print(type(x))
print(x)
x = 123 > 124
print(type(x))
print(x)
