import sys
from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QMessageBox,
    QInputDialog,
    QListWidgetItem,
)
from video482 import Ui_ComidasFavoritasEditor


class AplicacionEditorComidasFavoritas(QDialog):
    def __init__(self):
        super().__init__()
        self.inicializarGui()

    def inicializarGui(self):
        self.ui = Ui_ComidasFavoritasEditor()
        self.ui.setupUi(self)

        self.ui.btn_agregar.clicked.connect(self.agregar_comida)
        self.ui.btn_eliminar_todos.clicked.connect(self.eliminar_todos)
        self.ui.btn_editar.clicked.connect(self.editar_comida)
        self.ui.btn_eliminar.clicked.connect(self.eliminar_comida)

    def eliminar_comida(self):
        self.ui.lst_comidas_favoritas.takeItem(
            self.ui.lst_comidas_favoritas.currentRow()
        )

    def editar_comida(self):
        item_seleccionado = self.ui.lst_comidas_favoritas.currentRow()
        texto, resultado = QInputDialog.getText(
            self, "Editar Comida Favorita...", "Ingrese el nuevo nombre"
        )
        if resultado and len(texto.strip()):
            self.ui.lst_comidas_favoritas.takeItem(item_seleccionado)
            self.ui.lst_comidas_favoritas.insertItem(
                item_seleccionado, QListWidgetItem(texto)
            )

    def eliminar_todos(self):
        self.ui.lst_comidas_favoritas.clear()
        self.ui.btn_editar.setDisabled(True)
        self.ui.btn_eliminar.setDisabled(True)
        self.ui.btn_eliminar_todos.setDisabled(True)
        self.ui.txt_nombre_comida_favorita.clear()

    def agregar_comida(self):
        nombre_comida = self.ui.txt_nombre_comida_favorita.text().strip()
        if len(nombre_comida):
            self.ui.lst_comidas_favoritas.addItem(nombre_comida)
            self.ui.btn_editar.setEnabled(True)
            self.ui.btn_eliminar.setEnabled(True)
            self.ui.btn_eliminar_todos.setEnabled(True)
            self.ui.txt_nombre_comida_favorita.clear()
        else:
            mensaje = QMessageBox(self)
            mensaje.setIcon(QMessageBox.Warning)
            mensaje.setWindowTitle("Mensaje")
            mensaje.setText("El campo nombre comida favorita es obligatorio")
            mensaje.exec_()


def main():
    app = QApplication(sys.argv)
    ventana = AplicacionEditorComidasFavoritas()
    ventana.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
