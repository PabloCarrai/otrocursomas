import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap


class ImagenVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.inicializarGui()

    def inicializarGui(self):
        self.setWindowTitle("Logo pyqt")
        lbl_imagen = QLabel(self)
        imagen = QPixmap("/home/ed/otrocursomas/video-420/logo.png")
        lbl_imagen.setPixmap(imagen)
        self.resize(imagen.width(), imagen.height())
        self.setFixedWidth(imagen.width())
        self.setFixedHeight(imagen.height())


def main():
    app = QApplication(sys.argv)
    ventana = ImagenVentana()
    ventana.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
