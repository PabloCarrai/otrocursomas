import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from video474 import Ui_Heladeria


class AplicacionInicioSesion(QMainWindow):
    def __init__(self):
        super().__init__()
        self.inicializarGui()

    def inicializarGui(self):
        self.ui = Ui_Heladeria()
        self.ui.setupUi(self)


def main():
    app = QApplication(sys.argv)
    ventana = AplicacionInicioSesion()
    ventana.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()