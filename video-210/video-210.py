from random import randint as rd

aleatorioAdiviar = rd(1, 15)
print(aleatorioAdiviar)
intentos = 3
while intentos >= 1:
    numero = int(input("Adivine un numero entre el 1 y el 15  "))
    intentos -= 1
    if numero != aleatorioAdiviar:
        print(f"Tienes {intentos}")
    else:
        if numero == aleatorioAdiviar:
            print(f"Salio el {aleatorioAdiviar} y vos elegistes el {numero}")
            print("Felicitaciones adivinaste")
            break
