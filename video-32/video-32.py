puntaje = 300
x = -5
print(type(puntaje))
print(type(x))

print(f"El puntaje antes de la adicion es {puntaje}")
puntaje = puntaje + 50
print(f"El puntaje luego de la adicion es {puntaje}")
print(f"El tipo de variable de puntaje es {type(puntaje)}")

print(f"El puntaje de x antes de la adicion es {x}")
x += 10  # esto es igual a x = x + 10
print(f"El puntaje de x luego de la adicion es {x}")
print(f"El tipo de variable x es {type(x)}")

print("Uso de la clase int() para crear numeros enteros:")
edad = int(input("Escriba su edad:  "))
print(f"tipo de dato de la variable entrada {type(edad)}")
total_dias = edad * 365
print("Total de dias vividos hasta el momento: %i" % total_dias)
