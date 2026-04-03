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
        self.setFixedSize(400, 450)

        self.btn_nombre = QPushButton("Capturar Nombre", self)
        self.btn_nombre.move(100, 30)
        self.btn_nombre.setFixedWidth(200)
        self.btn_nombre.clicked.connect(self.capturar_nombre)

        self.btn_edad = QPushButton("Capturar Edad", self)
        self.btn_edad.move(100, 70)
        self.btn_edad.setFixedWidth(200)
        self.btn_edad.clicked.connect(self.capturar_edad)

        self.btn_ahorro = QPushButton("Capturar Ahorro", self)
        self.btn_ahorro.move(100, 110)
        self.btn_ahorro.setFixedWidth(200)
        self.btn_ahorro.clicked.connect(self.capturar_ahorro)

        self.btn_color = QPushButton("Capturar Color", self)
        self.btn_color.move(100, 150)
        self.btn_color.setFixedWidth(200)
        self.btn_color.clicked.connect(self.capturar_color)

        lbl_resumen = QLabel("Resumen:", self)
        lbl_resumen.move(180, 210)

        lbl_nombre = QLabel("Nombre:", self)
        lbl_nombre.move(30, 270)

        self.txt_nombre = QLineEdit(self)
        self.txt_nombre.move(170, 270)
        self.txt_nombre.setFixedWidth(200)
        self.txt_nombre.setEnabled(False)

        lbl_edad = QLabel("Edad:", self)
        lbl_edad.move(30, 310)

        self.txt_edad = QLineEdit(self)
        self.txt_edad.move(170, 310)
        self.txt_edad.setFixedWidth(200)
        self.txt_edad.setEnabled(False)

        lbl_ahorros = QLabel("Ahorros:", self)
        lbl_ahorros.move(30, 350)

        self.txt_ahorros = QLineEdit(self)
        self.txt_ahorros.move(170, 350)
        self.txt_ahorros.setFixedWidth(200)
        self.txt_ahorros.setEnabled(False)

        lbl_color = QLabel("Color:", self)
        lbl_color.move(30, 390)

        self.txt_color = QLineEdit(self)
        self.txt_color.move(170, 390)
        self.txt_color.setFixedWidth(200)
        self.txt_color.setEnabled(False)

    def capturar_nombre(self):
        pass

    def capturar_edad(self):
        pass

    def capturar_ahorro(self):
        pass

    def capturar_color(self):
        pass


def main():
    app = QApplication(sys.argv)
    ventana = CapturaDatosventana()
    ventana.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
