import sys
from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QWidget,
    QPushButton,
    QGridLayout,
    QGroupBox,
    QVBoxLayout,
)
from PyQt5.QtCore import pyqtSlot


class CalculadoraDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.inicializarGui()

    def inicializarGui(self):
        self.setWindowTitle("QGridLayout")
        self.setFixedSize(300, 150)

        self.crearBotones()
        layout = QVBoxLayout()
        layout.addWidget(self.gbx_controles)
        self.setLayout(layout)

    def crearBotones(self):
        self.gbx_controles = QGroupBox("Botones")
        layout = QGridLayout()

        btn_uno = QPushButton("1")
        btn_uno.clicked.connect(self.click)
        btn_dos = QPushButton("2")
        btn_dos.clicked.connect(self.click)
        btn_tres = QPushButton("3")
        btn_tres.clicked.connect(self.click)
        btn_cuatro = QPushButton("4")
        btn_cuatro.clicked.connect(self.click)
        btn_cinco = QPushButton("5")
        btn_cinco.clicked.connect(self.click)
        btn_seis = QPushButton("6")
        btn_seis.clicked.connect(self.click)
        btn_siete = QPushButton("7")
        btn_siete.clicked.connect(self.click)
        btn_ocho = QPushButton("8")
        btn_ocho.clicked.connect(self.click)
        btn_nueve = QPushButton("9")
        btn_nueve.clicked.connect(self.click)

        layout.addWidget(btn_uno, 0, 0)
        layout.addWidget(btn_dos, 0, 1)
        layout.addWidget(btn_tres, 0, 2)
        layout.addWidget(btn_cuatro, 1, 0)
        layout.addWidget(btn_cinco, 1, 1)
        layout.addWidget(btn_seis, 1, 2)
        layout.addWidget(btn_siete, 2, 0)
        layout.addWidget(btn_ocho, 2, 1)
        layout.addWidget(btn_nueve, 2, 2)

        self.gbx_controles.setLayout(layout)

    @pyqtSlot()
    def click(self):
        print("Se ha precionado un boton")


def main():
    app = QApplication(sys.argv)
    ventana = CalculadoraDialog()
    ventana.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
