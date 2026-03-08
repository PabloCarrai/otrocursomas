from modelos.empleado_horas import EmpleadoHoras
from modelos.empleado_nomina import EmpleadoNomina
from modelos.empleado_comision import EmpleadoComision


def main():
    empleados = []

    jorge = EmpleadoComision(
        "123", "Jorge Perez", "jorge@mail.com", "Ventas", 0.30, 10000
    )

    viviana = EmpleadoHoras(
        "987", "Viviana Garcia", "viviana@mail.com", "Diseño Grafico", 80, 100
    )

    patricia = EmpleadoNomina(
        "456", "Patricia Toledo", "patricia@mail.com", "Finanzas", 0.10
    )

    empleados.append(jorge)
    empleados.append(viviana)
    empleados.append(patricia)

    for empleado in empleados:
        print(empleado)
        print(f"Salario: ${empleado.calcular_salario()}")


if __name__ == "__main__":
    main()
