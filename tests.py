import pytest
from estacionamiento import *

def test_calculo_con_modificador():
    estadia1 = Estadia("AB123CD", 2)
    estadia1.agregar_modificador(Nocturno())
    assert estadia1.total(1000) == 2400


def test_validacion_horas_negativas():
    with pytest.raises(ValueError):
        Estadia("AB123CD", -1)


def test_rechaza_modificador_invalido():
    estadia2 = Estadia("AB123CD", 2)
    with pytest.raises(TypeError):
        estadia2.agregar_modificador("modificador")


def test_modificadores_es_inmutable():
    estadia3 = Estadia("AB123CD", 2)
    estadia3.agregar_modificador(Nocturno())

    tupla_externa = estadia3.modificador
    tupla_externa = tupla_externa + (FinDeSemana(),)

    assert estadia3.total(1000) == 2400


def test_mensual_validacion_de_horas():
    with pytest.raises(ValueError):
        Mensual("XY987ZW", -1, 20)


def test_mensual_con_descuento():
    mensual = Mensual("XY987ZW", 2, 20)
    mensual.agregar_modificador(Nocturno())
    assert mensual.total(1000) == 1920


def test_facturar_todo():
    estadias4 = Estadia("AB123CD", 2)
    estadias4.agregar_modificador(Nocturno())

    estadias5 = Mensual("XY987ZW", 2, 20)
    estadias5.agregar_modificador(Nocturno())

    juntas = [estadias4, estadias5]

    total = facturar_estadia(juntas, 1000)
    assert total == 2400 + 1920
