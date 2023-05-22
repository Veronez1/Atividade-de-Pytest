import pytest


def calcular_area_retangulo(comprimento, largura):
    return comprimento * largura


@pytest.mark.parametrize("comprimento, largura, area", [
    (2, 3, 6),  # Teste com números inteiros
    (0, 5, 0),  # Teste com zero
    (2.5, 4.5, 11.25),  # Teste com números decimais
    (-3, 2, -6),  # Teste com números negativos
])
def test_calcular_area_retangulo(comprimento, largura, area):
    assert calcular_area_retangulo(comprimento, largura) == area
