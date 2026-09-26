import sys
from PyQt5.QtWidgets import QApplication, QDialog, QLCDNumber
from PyQt5.QtCore import QTime, QTimer
from video488 import Ui_RelojDigital


class AplicacionRelojDigital(QDialog):
    def __init__(self):
        super().__init__()
        self.inicializarGui()

    def inicializarGui(self):
        self.ui = Ui_RelojDigital()
        self.ui.setupUi(self)

        timer = QTimer(self)
        timer.timeout.connect(self.tick)
        timer.start(1000)

    def tick(self):
        hora = QTime.currentTime()
        hora_texto = hora.toString("hh:mm")

        self.ui.lcd_hora.display(hora_texto)


def main():
    app = QApplication(sys.argv)
    ventana = AplicacionRelojDigital()
    ventana.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
