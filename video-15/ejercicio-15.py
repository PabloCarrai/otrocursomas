#   Primer programa posta
#   Creamos una funcion
def sumar(a, b):  #   def nombrefuncion(argumentos)
    suma = a + b  #   Creo una variable y sumo los argumentos
    return suma  #   Esto devuelve el valor de suma


numero1 = int(
    input("Ingrese el primer numero:   ")
)  # Esto devuelve caracteres, no numeros por eso el int
numero2 = int(
    input("Ingrese el segundo numero:   ")
)  # Esto devuelve caracteres, no numeros por eso el int
resultado = sumar(numero1, numero2)
print("La suma de {} y {} es igual a {}".format(numero1, numero2, resultado))
