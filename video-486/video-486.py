import sys
from PyQt5.QtWidgets import QApplication, QDialog
from video486 import Ui_GestorDescargas


class AplicacionGestorDescargas(QDialog):
    def __init__(self):
        super().__init__()
        self.inicializarGui()

    def inicializarGui(self):
        self.ui = Ui_GestorDescargas()
        self.ui.setupUi(self)

        self.ui.btn_iniciar_descargas.clicked.connect(self.iniciar_descarga)

    def iniciar_descarga(self):
        contador = 0
        while contador < 100:
            contador += 1
            self.ui.pbr_descargas.setValue(contador)


def main():
    app = QApplication(sys.argv)
    ventana = AplicacionGestorDescargas()
    ventana.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
