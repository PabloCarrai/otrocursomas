import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from PyQt5 import uic


class Aplicacion(QMainWindow):
    def __init__(self):
        super().__init__()

        self.inicializarGui()

    def inicializarGui(self):
        uic.loadUi("/home/ed/otrocursomas/video-560/video-560.ui", self)

        self.btn_saludar = self.findChild(QPushButton, "btn_saludar")
        self.btn_saludar.clicked.connect(self.saludar)
        self.show()

    def saludar(self):
        mensaje = QMessageBox(self)
        mensaje.setWindowTitle("Mensaje")
        mensaje.setIcon(QMessageBox.Information)
        mensaje.setText("Hola Usuario")
        mensaje.exec_()


def main():
    app = QApplication(sys.argv)
    ventana = Aplicacion()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
