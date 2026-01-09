# Division entre cero (ZeroDivisionError: division by zero)
numero = 5
numero1 = 0
if numero1 != 0:
    division = numero / numero1
    print(f"{division}")
else:
    print("No se puede dividir por cero")

try:
    division = numero / numero1
    print(f"{division}")
except ZeroDivisionError as err:
    print(err)
