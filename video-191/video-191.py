#   Categorizar segun la cantidad de puntos obtenidos por un jugador
#   0-100 principiante
#   101-500 Estandar
#   501-2000 Experimentado
#   2000> Master

cPuntos = int(input("Cuantos puntos obtuvo en total: ?  "))
calificacion = ("Principiante", "Estandar", "Experimentado", "Master")
if 0 <= cPuntos <= 100:
    print(f"Usted califica como {calificacion[0]}")
elif 101 <= cPuntos <= 500:
    print(f"Usted califica como {calificacion[1]}")
elif 501 <= cPuntos <= 2000:
    print(f"Usted califica como {calificacion[2]}")
elif cPuntos > 2000:
    print(f"Usted califica como {calificacion[3]}")
