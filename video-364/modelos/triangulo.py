from modelos.figura import Figura


class Triangulo(Figura):
    def __init__(self, colorFondo, colorBorde, base, altura):
        super().__init__(colorFondo, colorBorde)
        self.base = base
        self.altura = altura

    def dibujar(self):
        pass

    def area(self):
        pass
