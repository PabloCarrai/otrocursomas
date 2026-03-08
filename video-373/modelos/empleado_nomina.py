from modelos.empleado import Empleado


class EmpleadoNomina(Empleado):
    def __init__(
        self, documento, nombre_completo, correo_electronico,especialidad, porcentaje_prestaciones
    ):
        super().__init__(documento, nombre_completo, correo_electronico,especialidad)
        self.porcentaje_prestaciones = porcentaje_prestaciones

    def calcular_salario(self):
        return super().calcular_salario()
