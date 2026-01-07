#   Crea una seccion de una tupla usando notacion slicing(rebanada)
tupla_Original = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f"Tengo la tupla_Original que tiene {tupla_Original}")
print(f"Por las dudas su tipo es {type(tupla_Original)}")
tupla_rebanada = tupla_Original[1 : len(tupla_Original) - 1]
print(f"Ahora tengo la tupla_rebanada que tiene {tupla_rebanada}")
print(f"Por las dudas su tipo es {type(tupla_rebanada)}")
