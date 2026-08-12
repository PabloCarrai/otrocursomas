import sys
from PyQt5.QtWidgets import QApplication, QDialog
from video483 import Ui_Lenguajes


class AplicacionSeleccionLenguaje(QDialog):
    def __init__(self):
        super().__init__()
        self.inicializarGui()

    def inicializarGui(self):
        self.ui = Ui_Lenguajes()
        self.ui.setupUi(self)

        self.ui.cbx_lenguajes.currentIndexChanged.connect(self.seleccionar_lenguaje)

    def seleccionar_lenguaje(self):
        indice = self.ui.cbx_lenguajes.currentIndex()
        seleccion = self.ui.cbx_lenguajes.itemText(indice)

        self.ui.lbl_seleccion.setText(f"El lenguaje seleccionado es {seleccion}")


def main():
    app = QApplication(sys.argv)
    ventana = AplicacionSeleccionLenguaje()
    ventana.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
