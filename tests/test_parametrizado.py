import pytest

@pytest.mark.parametrize("a, b, resultado", [
    (1,2,3),
    (0,0,0),
    (-1, 1,0),
    (100, 200, 300)
])

def test_suma_parametrizada(a,b, resultado):
    assert a+b == resultado

# prueba la suma con diferentes combinaciones
# es eficiente para validar muchas entradas
