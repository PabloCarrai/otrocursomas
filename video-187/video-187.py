#   Comprobar el producto de mayor precio entre tres productos
producto1 = float(input("Ingrese el precio del primer producto "))
producto2 = float(input("Ingrese el precio del segundo producto "))
producto3 = float(input("Ingrese el precio del tercer producto "))
mayor = 0
if producto1 > producto2 and producto1 > producto3:
    mayor = producto1
    print(f"El producto 1 es mayor con el valor de ${mayor}")
elif producto2 > producto1 and producto2 > producto3:
    mayor = producto2
    print(f"El producto 2 es mayor con el valor de ${mayor}")
elif producto3 > producto1 and producto3 > producto2:
    mayor = producto3
    print(f"El producto 3 es mayor con el valor de ${mayor}")
else:
    print(f"Tienen el mismo valor")
