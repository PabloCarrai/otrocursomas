from modelos.figura import Figura


class Rectangulo(Figura):
    def __init__(self, colorFondo, colorBorde, ancho, alto):
        super().__init__(colorFondo, colorBorde)
        self.ancho = ancho
        self.alto = alto

    def dibujar(self):
        pass

    def area(self):
        pass
