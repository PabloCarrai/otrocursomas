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
        self.mni_salir.setShortcut("Ctrl+Q")
        self.mni_salir.setStatusTip("Finaliza la aplicacion")
        self.mni_salir.triggered.connect(self.close)

        self.mni_copiar = QAction("Copiar", self)
        self.mni_copiar.setShortcut("Ctrl+C")
        self.mnu_operaciones.addAction(self.mni_copiar)

        self.mni_cortar = QAction("Cortar", self)
        self.mni_cortar.setShortcut("Ctrl+X")
        self.mnu_operaciones.addAction(self.mni_cortar)

        self.mni_pegar = QAction("Pegar", self)
        self.mni_pegar.setShortcut("Ctrl+V")
        self.mnu_operaciones.addAction(self.mni_pegar)

        self.mnu_archivo.addAction(self.mni_salir)

        self.mni_acerca_de = QAction("Acerca de...")
        self.mnu_ayuda.addAction(self.mni_acerca_de)
        self.mni_acerca_de.triggered.connect(self.mostrar_acerca_de)

    def mostrar_acerca_de(self):
        mensaje = QMessageBox()
        mensaje.setWindowTitle("Acerca de ....")
        mensaje.setIcon(QMessageBox.Information)
        mensaje.setText("Desarrollador: Pablo Carrai")
        mensaje.exec_()


def main():
    app = QApplication(sys.argv)
    ventana = AplicacionVentana()
    ventana.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
