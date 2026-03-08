from modelos.figura import Figura


class Rectangulo(Figura):
    def __init__(self, color_fondo, color_borde, ancho, alto):
        super().__init__(color_fondo, color_borde)
        self.ancho = ancho
        self.alto = alto

    def dibujar(self):
        print(
            f"Se esta dibujando el Rectangulo con medidas ancho: {self.ancho}, y alto: {self.alto}"
        )

    def area(self):
        resultado = self.ancho * self.alto
        return resultado

    def __str__(self):
        #   Aca al original de __str__ le agrega su propia parte
        return f"Rectangulo -- {super().__str__()} - Ancho: {self.ancho}- Alto: {self.alto}"
