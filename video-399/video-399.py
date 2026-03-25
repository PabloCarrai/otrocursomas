import sys
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMessageBox,
    QMainWindow,
    QPushButton,
)


class CalculadoraVentana(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.initUi()

    def initUi(self):
        self.setWindowTitle("Calculadora Basica")
        self.setFixedSize(400, 300)

        self.lbl_primer_numero = QLabel("Primer numero:  ", self)
        self.lbl_primer_numero.move(30, 30)

        self.txt_primer_numero = QLineEdit(self)
        self.txt_primer_numero.move(150, 30)
        self.txt_primer_numero.setFixedWidth(200)

        self.lbl_segundo_numero = QLabel("Segundo numero:  ", self)
        self.lbl_segundo_numero.move(30, 80)

        self.txt_segundo_numero = QLineEdit(self)
        self.txt_segundo_numero.move(150, 80)
        self.txt_segundo_numero.setFixedWidth(200)

        self.btn_calcular_suma = QPushButton("Sumar", self)
        self.btn_calcular_suma.move(150, 130)
        self.btn_calcular_suma.setFixedWidth(200)
        self.btn_calcular_suma.clicked(self.sumar)

        self.lbl_resultado = QLabel("Resultado", self)
        self.lbl_resultado.move(30, 230)

        self.txt_resultado = QLineEdit(self)
        self.txt_resultado.move(150, 200)
        self.txt_resultado.setFixedWidth(200)

    def sumar(self):
        primer_numero = self.txt_primer_numero.text().strip()
        segimdp_numero = self.txt_segundo_numero.text().strip()

        mensaje = QMessageBox()
        mensaje.setWindowTitle("Informacion")

        if len(primer_numero):
            if len(self.lbl_segundo_numero):
                try:
                    segundo_numero = float(segundo_numero)
                except:
                    mensaje.setIcon(QMessageBox.Warning)
                    mensaje.setText("El campo segundo numero Debe ser numerico")
                    return
                try:
                    primer_numero = float(primer_numero)
                except:
                    mensaje.setIcon(QMessageBox.Warning)
                    mensaje.setText("El campo primer numero Debe ser numerico")
                    return

            else:
                mensaje.setIcon(QMessageBox.Warning)
                mensaje.setText("El campo segundo numero es obligatorio")
        else:
            mensaje.setIcon(QMessageBox.Warning)
            mensaje.setText("El campo primer numero es obligatorio")


def main():
    app = QApplication(sys.argv)
    calculadora = CalculadoraVentana()
    calculadora.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
