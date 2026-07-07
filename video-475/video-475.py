import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from video475 import Ui_SegnialesSlots


class Aplicacion(QMainWindow):
    def __init__(self):
        super().__init__()
        self.inicializarGui()

    def inicializarGui(self):
        self.ui = Ui_SegnialesSlots()
        self.ui.setupUi(self)


def main():
    app = QApplication(sys.argv)
    ventana = Aplicacion()
    ventana.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
