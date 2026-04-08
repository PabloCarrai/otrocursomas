import sys
from PyQt5.QtWidgets import (
    QApplication,
    QRadioButton,
    QLabel,
    QMainWindow,
)


class SeleccionClaseVueloVentana(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.inicializarGui()

    def inicializarGui(self):
        self.setWindowTitle("Seleccion Clase Vuelo  ")
        self.setFixedSize(350, 300)

        lbl_seleccion_clase_vuelo = QLabel("Seleccione la clase de su vuelo", self)
        lbl_seleccion_clase_vuelo.move(30, 30)
        lbl_seleccion_clase_vuelo.setFixedWidth(200)

        self.rbn_clase_primera = QRadioButton("Primera Clase", self)
        self.rbn_clase_primera.move(30, 80)
        self.rbn_clase_primera.adjustSize()
        self.rbn_clase_primera.toggled.connect(self.seleccionar_clase)

        self.rbn_clase_negocio = QRadioButton("Clase Negocio", self)
        self.rbn_clase_negocio.move(30, 110)
        self.rbn_clase_negocio.adjustSize()
        self.rbn_clase_negocio.toggled.connect(self.seleccionar_clase)

        self.rbn_clase_economica = QRadioButton("Clase Economica", self)
        self.rbn_clase_economica.move(30, 140)
        self.rbn_clase_economica.adjustSize()
        self.rbn_clase_economica.toggled.connect(self.seleccionar_clase)

        self.lbl_resultado_seleccion = QLabel("", self)
        self.lbl_resultado_seleccion.move(30, 180)
        self.lbl_resultado_seleccion.setFixedWidth(250)

    def seleccionar_clase(self):
        costo_vuelo = 0
        if self.rbn_clase_primera.isChecked():
            costo_vuelo = 2000
        if self.rbn_clase_negocio.isChecked():
            costo_vuelo = 1500
        if self.rbn_clase_economica.isChecked():
            costo_vuelo = 1000
        self.lbl_resultado_seleccion.setText(f"Costo del Vuelo: {costo_vuelo}")


def main():
    app = QApplication(sys.argv)
    ventana = SeleccionClaseVueloVentana()
    ventana.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
