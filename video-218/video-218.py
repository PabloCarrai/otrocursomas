#   Contar la cantidad de digitos y letras que tiene un texto

contadorDigitos = 0
contadorCaracter = 0
frase = input("Ingrese una palabra o frase    ")
for e in range(len(frase)):
    if frase[e].isnumeric():
        contadorDigitos += 1
    else:
        if frase[e].isalpha:
            contadorCaracter += 1

print(f"La frase original es {frase}")
print(f"Cantidad de Digitos {contadorDigitos}")
print(f"Cantidad de Caracteres {contadorCaracter}")
