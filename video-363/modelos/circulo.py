from modelos.figura import Figura


class Circulo(Figura):
    def __init__(self, colorFondo, colorBorde, radio):
        super().__init__(colorFondo, colorBorde)
        self.radio = radio

    def dibujar(self):
        pass

    def area(self):
        pass
