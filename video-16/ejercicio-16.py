def sumar(a, b):
    suma = a + b
    return suma


numero1 = float(input("Ingrese el primer numero:   "))
numero2 = float(input("Ingrese el segundo numero:   "))
resultado = sumar(numero1, numero2)
print("La suma de {} y {} es igual a {}".format(numero1, numero2, resultado))
