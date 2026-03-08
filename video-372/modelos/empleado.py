from abc import ABC, abstractmethod


class Empleado(ABC):
    def __init__(self, documento, nombre_completo, correo_electronico,especialidad):
        self.documento = documento
        self.nombre_completo = nombre_completo
        self.correo_electronico = correo_electronico
        self.especialidad=especialidad

    @abstractmethod
    def calcular_salario(self):
        pass
