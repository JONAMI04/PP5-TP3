class Estadia:
    def __init__(self, patente, horas_en_guarda):
        self._dominio = None
        self._horas = None
        self._modif = []
        self.ver_patente = patente
        self.horas = horas_en_guarda

    @property
    def modificador(self):
        return tuple(self._modif)

    @property
    def ver_patente(self):
        return self._dominio

    @property
    def horas(self):
        return self._horas

    @ver_patente.setter
    def ver_patente(self, patente):
        if patente.strip() == "":
            raise ValueError ("Error el domino no puede estar vacio")
        self._dominio = patente

    @horas.setter
    def horas(self, horas_en_guarda):
        if horas_en_guarda <= 0:
            raise ValueError ("Error no pueden ser menos o iguales a 0 las horas")
        self._horas = horas_en_guarda

    def agregar_modificador(self, modificador):
        if not hasattr(modificador, "aplicar") or not callable(modificador.aplicar):
            raise TypeError("El modificador no es válido.")
        self._modif.append(modificador)

    def total(self, valor_hora):
        total = 0
        if valor_hora <= 0:
            raise ValueError("Error la tarifa no puede ser menor o igual a 0")
        total = valor_hora * self.horas
        for modificador in self.modificador:
            total = modificador.aplicar(total, self.horas)
        return total