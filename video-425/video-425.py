import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiSubWindow, QAction, QMdiArea


class MdiAplicacion(QMainWindow):

    contador = 0

    def __init__(self):
        super().__init__()

        self.inicializarGui()

    def inicializarGui(self):
        self.setWindowTitle("Ventana MDI: Multipe Document Interface")
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        mbr_principal = self.menuBar()
        mnu_archivo = mbr_principal.addMenu("Archivo")

        mni_agregar_ventana = QAction("Agregar ventana", self)
        mni_agregar_ventana.triggered.connect(self.agregar_ventana)

        mni_salir = QAction("Salir", self)
        mni_salir.setShortcut("Ctrl+Q")
        mni_salir.triggered.connect(self.close)

        mnu_archivo.addAction(mni_agregar_ventana)
        mnu_archivo.addAction(mni_salir)

    def agregar_ventana(self):
        MdiAplicacion.contador += 1
        subventana = QMdiSubWindow()
        subventana.setWindowTitle(f"Subventana {MdiAplicacion.contador}")
        self.mdi.addSubWindow(subventana)
        subventana.show()


def main():
    app = QApplication(sys.argv)
    ventana = MdiAplicacion()
    ventana.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
