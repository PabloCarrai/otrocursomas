import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtGui import QFont
from video485 import Ui_EditorTexto


class AplicacionEditorTexto(QDialog):
    def __init__(self):
        super().__init__()
        self.inicializarGui()

    def inicializarGui(self):
        self.ui = Ui_EditorTexto()
        self.ui.setupUi(self)

        indice = self.ui.fcb_fuentes.currentIndex()
        fuente = QFont(self.ui.fcb_fuentes.itemText(indice), 15)
        self.ui.txt_editor.setFont(fuente)
        self.ui.fcb_fuentes.currentFontChanged.connect(self.cambiar_fuente)

    def cambiar_fuente(self):
        indice = self.ui.fcb_fuentes.currentIndex()
        fuente = QFont(self.ui.fcb_fuentes.itemText(indice), 15)
        self.ui.txt_editor.setFont(fuente)


def main():
    app = QApplication(sys.argv)
    ventana = AplicacionEditorTexto()
    ventana.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
