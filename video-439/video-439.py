import sys
from PyQt5.QtWidgets import (
    QApplication,
    QTabWidget,
    QLineEdit,
    QWidget,
    QFormLayout,
    QRadioButton,
    QHBoxLayout,
    QComboBox,
    QPushButton,
)


class CapturaDatos(QTabWidget):
    def __init__(self):
        super().__init__()
        self.inicializarGui()

    def inicializarGui(self):
        self.setWindowTitle("Captura Datos Basicos")
        self.setFixedSize(360, 360)

        self.tab_datos_basicos = QWidget()
        self.tab_datos_contacto = QWidget()
        self.tab_datos_educacion = QWidget()

        self.addTab(self.tab_datos_basicos, "Basicos")
        self.addTab(self.tab_datos_contacto, "Contacto")
        self.addTab(self.tab_datos_educacion, "Educacion")

        self.inicializar_tab_datos_basicos()
        self.inicializar_tab_datos_contacto()
        self.inicializar_tab_datos_educacion()

    def inicializar_tab_datos_basicos(self):
        layout = QFormLayout()
        layout.addRow("Nombre:", QLineEdit())
        layout.addRow("Apellido:", QLineEdit())

        lay_genero = QHBoxLayout()
        lay_genero.addWidget(QRadioButton("Hombre"))
        lay_genero.addWidget(QRadioButton("Mujer"))
        layout.addRow("Genero", lay_genero)
        self.tab_datos_basicos.setLayout(layout)

    def inicializar_tab_datos_contacto(self):
        layout = QFormLayout()
        layout.addRow("Correo-E:", QLineEdit())
        layout.addRow("Direccion:", QLineEdit())
        self.tab_datos_contacto.setLayout(layout)

    def inicializar_tab_datos_educacion(self):
        layout = QFormLayout()
        cbx_nivel_educativo = QComboBox()
        cbx_nivel_educativo.addItem("Primaria")
        cbx_nivel_educativo.addItem("Secundaria")
        cbx_nivel_educativo.addItem("Profesional")
        cbx_nivel_educativo.addItem("Maestria")
        cbx_nivel_educativo.addItem("Doctorado")
        layout.addRow("Nivel educativo: ", cbx_nivel_educativo)
        layout.addRow("Profesion: ", QLineEdit())
        layout.addRow("", QPushButton("Guardar Datos"))

        self.tab_datos_educacion.setLayout(layout)


def main():
    app = QApplication(sys.argv)
    ventana = CapturaDatos()
    ventana.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
