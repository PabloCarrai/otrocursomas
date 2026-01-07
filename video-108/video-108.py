#   Remover un elemento(valor) de una tupla
tupla_Original = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f"Tengo la tupla_Original que tiene {tupla_Original}")
tuplaEnLista = list(tupla_Original)
elemento = int(input(f"Que elemento eliminamos de la tupla {tupla_Original} ?"))
tuplaEnLista.remove(elemento)
tupla_Resultante = tuple(tuplaEnLista)
print(f"Quedo como  {tupla_Resultante}")
