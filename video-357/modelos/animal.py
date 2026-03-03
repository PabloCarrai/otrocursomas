from abc import ABC, abstractmethod  # necesaria para la parte abstracta


class Animal(ABC):  # Debe heredar de ahi
    def __init__(self, nombre, edad, nombre_cientifico):
        self.nombre = nombre
        self.edad = edad
        self.nombre_cientifico = nombre_cientifico

    def comer(self):
        print("El animal esta comiendo...")

    def moverse(self):
        print("El animal se esta moviendo...")

    @abstractmethod  #   Se requiere para ser abstracto
    def hablar(self):  #   Solo se implementa en las hijas(metodo abstracto)
        pass
