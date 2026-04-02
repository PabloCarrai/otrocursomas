import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QAction


class AplicacionVentana(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.inicializarGui()

    def inicializarGui(self):
        self.setWindowTitle("Aplicacion Principal")
        self.setFixedSize(500, 400)

        self.mbr_principal = self.menuBar()
        self.mnu_archivo = self.mbr_principal.addMenu("Archivo")
        self.mnu_operaciones = self.mbr_principal.addMenu("Operaciones")
        self.mnu_ayuda = self.mbr_principal.addMenu("Ayuda")

        self.mni_salir = QAction("Salir", self)
        self.mni_salir.setShortcut("Ctr+Q")
        self.mni_salir.setStatusTip("Finaliza la aplicacion")
        self.mni_salir.triggered.connect(self.close)

        self.mnu_archivo.addAction(self.mni_salir)


def main():
    app = QApplication(sys.argv)
    ventana = AplicacionVentana()
    ventana.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
