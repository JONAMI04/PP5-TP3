from functools import total_ordering

import estadia

class Mensual(estadia.Estadia):
    def __init__(self, patente, horas_en_guarda, descuento):
        super().__init__(patente, horas_en_guarda)
        self._descuento = None
        self.descuento = descuento
        self._modif = []

    @property
    def Descuento(self):
        return self._descuento

    @Descuento.setter
    def descuento(self,descuento):
        if descuento < 0 or descuento > 100:
            raise ValueError("Error el descuento no puede ser menor a 0 ni mayor a 100")
        self._descuento = descuento

    def total(self, tarifa_base):
        return (super().total(tarifa_base))*(1-self.descuento/100)
