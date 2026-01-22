#   Capturar la temperatura(sea en grados celcius, o farenheit)
#   y convertirla a la escala contraria.
#   Grados a farenheit se multiplica por 9 se divide por 5 y se suma 32
#   al reves es restar 32 multiplicar por 5/9
escala = int(input("A que escala quieres convertir 1)Celcius 2)Farenheit "))
if escala == 1:
    grados = float(input("Ingresa los grados asi los convertimos"))
    # conversion de grados a farenheit
    resultado = grados * 9 / 5 + 32
    print(f"Convertiendo los grados {grados} a farenheit tengo {resultado}")
else:
    if escala == 2:
        grados = float(input("Ingresa los grados asi los convertimos"))
        # conversion de farenheit a grados
        resultado = (grados - 32) * (5 / 9)
        print(f"Convertiendo los Farenheit {grados} a grados tengo {resultado}")
    else:
        print("Las respuestas posibles son 1 o 2 ")
print("Finalizado el programa")
