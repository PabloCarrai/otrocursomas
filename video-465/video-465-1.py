import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from video465 import Ui_CalculadoraBasicaVentana


class AplicacionVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.inicializarGui()

    def inicializarGui(self):
        self.ui = Ui_CalculadoraBasicaVentana()
        self.ui.setupUi(self)

        self.ui.btn_sumar.clicked.connect(self.sumar)

        self.show()

    def sumar(self):
        numero1 = float(self.ui.txt_numero_1.text())
        numero2 = float(self.ui.txt_numero_2.text())
        suma = numero1 + numero2
        self.ui.txt_resultado.setText(str(suma))


def main():
    app = QApplication(sys.argv)
    ventana = AplicacionVentana()
    ventana.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
