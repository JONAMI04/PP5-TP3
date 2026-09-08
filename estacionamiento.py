from abc import ABC, abstractmethod
from Mensual import Mensual
from estadia import Estadia


class ModificadorTarifa(ABC):
    @abstractmethod
    def aplicar(self, total: float, horas: int) -> float:
        """Devuelve el nuevo total."""





class Nocturno(ModificadorTarifa):
    def aplicar(self, total, horas):
        return total+200*horas

class FinDeSemana(ModificadorTarifa):
    def aplicar(self, total, horas):
        return total*1.5



def facturar_estadia(lista_estadias, tarifa_hora):
    factura = 0
    for estadia in lista_estadias:
        factura += estadia.total(tarifa_hora)
    return factura

estadias = []
estadia1 = Mensual("ABC123", 2, 20)
estadia1.agregar_modificador(Nocturno())

estadia2 = Estadia("DEF456", 3)
estadia2.agregar_modificador(FinDeSemana())
estadias.append(estadia2)

fact = facturar_estadia(estadias, 200)
print(f"El total de la factura es: {fact}")