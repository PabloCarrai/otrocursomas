import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QAction,
    QPlainTextEdit,
    QFileDialog,
)
from PyQt5.QtGui import QIcon


class BarraHerramientaVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.inicializarGui()

    def inicializarGui(self):
        self.setWindowTitle("Editor Basico de Texto")
        self.setFixedSize(400, 300)
        barra_herramientas = self.addToolBar("Archivo")
        mni_nuevo_archivo = QAction(
            QIcon("/home/ed/otrocursomas/video-432/nuevo.png"), "Nuevo", self
        )
        mni_nuevo_archivo.triggered.connect(self.crear_archivo)
        barra_herramientas.addAction(mni_nuevo_archivo)
        mni_abrir_archivo = QAction(
            QIcon("/home/ed/otrocursomas/video-432/abrir.png"), "Abrir", self
        )
        mni_abrir_archivo.triggered.connect(self.abrir_archivo)
        barra_herramientas.addAction(mni_abrir_archivo)
        mni_guardar_archivo = QAction(
            QIcon("/home/ed/otrocursomas/video-432/guardar.png"), "Guardar", self
        )
        mni_guardar_archivo.triggered.connect(self.guardar_archivo)
        barra_herramientas.addAction(mni_guardar_archivo)
        self.contenido = QPlainTextEdit(self)
        self.contenido.move(10, 50)
        self.contenido.setFixedWidth(380)
        self.contenido.setFixedHeight(250)

    def crear_archivo(self):
        self.contenido.clear()

    def abrir_archivo(self):
        archivo, ok = QFileDialog.getOpenFileName(
            self,
            "Seleccionar archivo de texto...",
            "/home/ed/",
            "Archivo de texto(*.txt)",
        )
        if ok:
            with open(archivo, "r") as f:
                self.contenido.insertPlainText("".join(f.readlines()))

    def guardar_archivo(self):
        archivo, ok = QFileDialog.getSaveFileName(
            self, "Guardar archivo de texto...", "/home/ed/", "Archivo de texto(*.txt)"
        )
        if ok:
            with open(archivo, "w") as f:
                f.write(self.contenido.toPlainText())


def main():
    app = QApplication(sys.argv)
    ventana = BarraHerramientaVentana()
    ventana.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
