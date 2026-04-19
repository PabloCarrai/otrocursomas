import sys
from PyQt5.QtWidgets import QApplication, QTabWidget, QLineEdit, QWidget


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
        pass

    def inicializar_tab_datos_contacto(self):
        pass

    def inicializar_tab_datos_educacion(self):
        pass


def main():
    app = QApplication(sys.argv)
    ventana = CapturaDatos()
    ventana.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
