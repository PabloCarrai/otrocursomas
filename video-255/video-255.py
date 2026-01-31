# expresiones lambda(Funciones anonimas)


def sumar(a, b):
    return a + b


x = 2
y = 3
print(f"La suma de {x} + {y} es igual a {sumar(x,y)}")


#   Ahora con lambda
sumar_lambda = lambda a, b: a + b
print(f"La suma de {x} + {y} es igual a {sumar_lambda(x,y)}")
