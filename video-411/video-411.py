import sys
from PyQt5.QtWidgets import (
    QApplication,
    QInputDialog,
    QLabel,
    QMainWindow,
    QLineEdit,
    QPushButton,
)


class CapturaDatosventana(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.inicializarGui()

    def inicializarGui(self):
        self.setWindowTitle("Captura de Datos - QInputDialog")
        self.setFixedSize(400, 500)

        self.btn_nombre = QPushButton("Capturar Nombre", self)
        self.btn_nombre.move(100, 30)
        self.btn_nombre.setFixedWidth(200)

        self.btn_edad = QPushButton("Capturar Edad", self)
        self.btn_edad.move(100, 70)
        self.btn_edad.setFixedWidth(200)

        self.btn_ahorro = QPushButton("Capturar Ahorro", self)
        self.btn_ahorro.move(100, 110)
        self.btn_ahorro.setFixedWidth(200)

        self.btn_color = QPushButton("Capturar Color", self)
        self.btn_color.move(100, 150)
        self.btn_color.setFixedWidth(200)

        lbl_resumen = QLabel("Resumen:", self)
        lbl_resumen.move(180, 210)

        lbl_nombre = QLabel("Nombre:", self)
        lbl_nombre.move(30, 270)

        self.txt_nombre = QLineEdit(self)
        self.txt_nombre.move(170, 270)
        self.txt_nombre.setFixedWidth(200)
        self.txt_nombre.setEnabled(False)


def main():
    app = QApplication(sys.argv)
    ventana = CapturaDatosventana()
    ventana.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
