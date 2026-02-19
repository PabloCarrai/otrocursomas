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
