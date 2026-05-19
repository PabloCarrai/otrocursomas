import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from video469 import Ui_VentaVentana


class AplicacionVentaVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.inicializarGui()

    def inicializarGui(self):
        self.ui = Ui_VentaVentana()
        self.ui.setupUi(self)

        self.ui.rbn_m.toggled.connect(self.mostrar_resultado)
        self.ui.rbn_l.toggled.connect(self.mostrar_resultado)
        self.ui.rbn_xl.toggled.connect(self.mostrar_resultado)
        self.ui.rbn_xll.toggled.connect(self.mostrar_resultado)

        self.ui.rbn_tarjeta_credito_debito.toggled.connect(self.mostrar_resultado)
        self.ui.rbn_pago_contra_entrega.toggled.connect(self.mostrar_resultado)
        self.ui.rbn_efectivo.toggled.connect(self.mostrar_resultado)
        self.ui.rbn_consigna_bancaria.toggled.connect(self.mostrar_resultado)

        self.show()

    def mostrar_resultado(self):
        talla = ""
        metodo_pago = "Efectivo"
        if self.ui.rbn_m.isChecked():
            talla = "m"
        if self.ui.rbn_l.isChecked():
            talla = "l"
        if self.ui.rbn_xl.isChecked():
            talla = "XL"
        if self.ui.rbn_xll.isChecked():
            talla = "XLL"
        if self.ui.rbn_tarjeta_credito_debito.isChecked():
            metodo_pago = "Tarjeta Credito/Debito"
        if self.ui.rbn_pago_contra_entrega.isChecked():
            metodo_pago = "Pago Contraentrega"
        if self.ui.rbn_consigna_bancaria.isChecked():
            metodo_pago = "Consignacion Bancaria"
        if self.ui.rbn_efectivo.isChecked():
            metodo_pago = "Efectivo"

        self.ui.lbl_seleccion.setText(
            f"La talla seleccionada es {talla} y metodo de pago {metodo_pago}"
        )


def main():
    app = QApplication(sys.argv)
    ventana = AplicacionVentaVentana()
    ventana.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
