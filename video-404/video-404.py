import sys
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMessageBox,
    QMainWindow,
    QPushButton,
)
from PyQt5.QtGui import QIntValidator


class EliminacionProductoVentana(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.initGui()

    def initGui(self):
        self.setWindowTitle("Eliminacion Producto Por Id")
        self.setFixedSize(400, 350)


def main():
    app = QApplication(sys.argv)
    ventana = EliminacionProductoVentana()
    ventana.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
