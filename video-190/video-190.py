#   Aplicar descuento segun la cantidad de productos comprados.
#   Cada producto cuesta 100000:
cProductos = int(input("Cuantos productos compraste?   "))
totalBruto = cProductos * 100000
descuento = 0
if 0 < cProductos < 10:
    descuento = totalBruto * (10 / 100)
    print(f"Usted compro {cProductos} a $100000")
    print(f"El total bruto de la compra es ${totalBruto}")
    print(f"Por esa cantidad el descuento es del %10 seria ${descuento} ")
    print(f"Su factura debera de pagar ${totalBruto-descuento}")
elif 10 <= cProductos <= 20:
    descuento = totalBruto * (25 / 100)
    print(f"Usted compro {cProductos} a $100000")
    print(f"El total bruto de la compra es ${totalBruto}")
    print(f"Por esa cantidad el descuento es del %25 seria ${descuento} ")
    print(f"Su factura debera de pagar ${totalBruto-descuento}")
elif 21 <= cProductos <= 30:
    descuento = totalBruto * (35 / 100)
    print(f"Usted compro {cProductos} a $100000")
    print(f"El total bruto de la compra es ${totalBruto}")
    print(f"Por esa cantidad el descuento es del %35 seria ${descuento} ")
    print(f"Su factura debera de pagar ${totalBruto-descuento}")
