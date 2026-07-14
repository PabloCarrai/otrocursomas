import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from PyQt5.QtGui import QDoubleValidator
from video476 import Ui_Calculadora


class AplicacionCalculadora(QMainWindow):
    def __init__(self):
        super().__init__()
        self.inicializarGui()

    def inicializarGui(self):
        self.ui = Ui_Calculadora()
        self.ui.setupUi(self)

        self.ui.btn_sumar.clicked.connect(self.sumar)
        self.ui.btn_restar.clicked.connect(self.restar)
        self.ui.btn_multiplicar.clicked.connect(self.multiplicar)
        self.ui.btn_dividir.clicked.connect(self.dividir)

        self.ui.txt_primer_numero.setValidator(QDoubleValidator())
        self.ui.txt_segundo_numero.setValidator(QDoubleValidator())

    def sumar(self):
        primer_numero = float(self.ui.txt_primer_numero.text())
        segundo_numero = float(self.ui.txt_segundo_numero.text())
        self.ui.label_3.setText(f"{primer_numero+segundo_numero}")

    def restar(self):
        primer_numero = float(self.ui.txt_primer_numero.text())
        segundo_numero = float(self.ui.txt_segundo_numero.text())
        self.ui.label_3.setText(f"{primer_numero-segundo_numero}")

    def dividir(self):
        primer_numero = float(self.ui.txt_primer_numero.text())
        segundo_numero = float(self.ui.txt_segundo_numero.text())
        if segundo_numero != 0:
            self.ui.label_3.setText(f"{primer_numero/segundo_numero}")
        else:
            self.ui.label_3.setText("No se puede dividir por 0")

    def multiplicar(self):
        primer_numero = float(self.ui.txt_primer_numero.text())
        segundo_numero = float(self.ui.txt_segundo_numero.text())
        self.ui.label_3.setText(f"{primer_numero*segundo_numero}")


def main():
    app = QApplication(sys.argv)
    ventana = AplicacionCalculadora()
    ventana.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
