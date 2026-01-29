#   Pasar argumento por valor y por referencias
print("#   Pasar argumento por valor y por referencias")


def duplicar(numero):
    numero *= 2
    print(f"El numero duplicado es igual a {numero}")


x = 2
print(f"x : {x}")
duplicar(x)  # No toca la original, es otro ambito
print(f"x : {x}")
