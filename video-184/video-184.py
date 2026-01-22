#   Condiciones compuesta operador logico or
agnios_experiencia = int(input("Años de experiencia programando: "))
lenguaje = input("Que lenguaje domina? ")
#   Con que una de las dos condiciones de true(se cumpla) se pasa al codigo siguiente
if agnios_experiencia >= 5 or lenguaje in ["python", "c", "c++"]:
    print("Usted califica para trabajar con nosotros ")
else:
    print("Usted no califica para trabajar con nosotros ")
