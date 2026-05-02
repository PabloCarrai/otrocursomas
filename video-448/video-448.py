import sys
from PyQt5.QtWidgets import (
    QApplication,
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QSpinBox,
    QGroupBox,
    QLabel,
    QVBoxLayout,
    QMessageBox,
)


class RegistroDialogo(QDialog):
    def __init__(self):
        super().__init__()
        self.inicializarGui()

    def inicializarGui(self):
        self.setWindowTitle("Registro Datos")
        self.setFixedSize(400, 150)
        self.crearFormularioRegistro()
        botones = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        botones.accepted.connect(self.registrar)
        botones.rejected.connect(self.cancelar)

        layout = QVBoxLayout()
        layout.addWidget(self.gbx_controles)
        layout.addWidget(botones)
        self.setLayout(layout)

    def registrar(self):
        mensaje = QMessageBox(self)
        mensaje.setIcon(QMessageBox.Information)
        mensaje.setWindowTitle("Mensaje")
        mensaje.setText("Los datos se registraron de forma correcta")
        mensaje.exec_()

    def cancelar(self):
        mensaje = QMessageBox(self)
        mensaje.setIcon(QMessageBox.Warning)
        mensaje.setWindowTitle("Advertencia")
        mensaje.setText("Datos sin registrarse")
        mensaje.exec_()

    def crearFormularioRegistro(self):
        self.gbx_controles = QGroupBox("Datos Basicos")
        layout = QFormLayout()
        layout.addRow(QLabel("Nombre:"), QLineEdit())
        paises = QComboBox()
        paises.addItem("Colombia")
        paises.addItem("Chile")
        paises.addItem("China")
        paises.addItem("Rusia")
        paises.addItem("Cuba")
        layout.addRow(QLabel("Pais:"), paises)
        layout.addRow(QLabel("Edad:"), QSpinBox())
        self.gbx_controles.setLayout(layout)


def main():
    app = QApplication(sys.argv)
    ventana = RegistroDialogo()
    ventana.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
