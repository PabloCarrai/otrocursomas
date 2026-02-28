class Animal:
    def __init__(self, nombre, edad, nombre_cientifico):
        self.nombre = nombre
        self.edad = edad
        self.nombre_cientifico = nombre_cientifico

    def comer(self):
        pass

    def moverse(self):
        pass

    def hablar(self):  # Solo se implementa en las hijas(metodo abstracto)
        pass
