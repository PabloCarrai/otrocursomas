#   Excepcion personalizada

print("Excepcion personalizada")


class ValorMinimoError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f"ValorMinimoError {self.message}"
        else:
            return "Se ha generado el error ValorMinimoError."

class ValorMaximoError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f"ValorMaximoError {self.message}"
        else:
            return "Se ha generado el error ValorMaximoError."