class Carro:  #   Primer letra en mayuscula
    def __init__(
        self, placa, marca, modelo, pais_procedencia
    ):  #   self representa el objeto actual
        #   atributos
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.pais_procedencia = pais_procedencia
        self.estado = False  # no se pasa en la instanciacion

    # metodos
    def encender(self):
        if not self.estado:
            self.estado = (
                True  # Estoy accediendo a un atributo de la clase y cambiando su valor
            )

    def apagar(self):
        if self.estado:
            self.estado = False

    def acelerar(self):
        if self.estado:
            print("El carro ha acelerado")

    def frenar(self):
        if self.estado:
            print("El carro ha frenado")
