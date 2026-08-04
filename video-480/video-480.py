import sys
from PyQt5.QtWidgets import QApplication, QDialog
from video480 import Ui_Diagnosticos


class AplicacionDiagnostico(QDialog):
    def __init__(self):
        super().__init__()
        self.inicializarGui()

    def inicializarGui(self):
        self.ui = Ui_Diagnosticos()
        self.ui.setupUi(self)

        self.ui.lst_diagnosticos.itemSelectionChanged.connect(
            self.seleccionar_diagnosticos
        )

    def seleccionar_diagnosticos(self):
        self.ui.lst_diagnosticos_seleccionados.clear()
        diagnosticos = list(self.ui.lst_diagnosticos.selectedItems())
        for d in diagnosticos:
            self.ui.lst_diagnosticos_seleccionados.addItem(d.text())


def main():
    app = QApplication(sys.argv)
    ventana = AplicacionDiagnostico()
    ventana.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
