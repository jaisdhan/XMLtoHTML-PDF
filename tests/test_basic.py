def sum(a,b):
    return a+b

def test_correct_sum():
    assert sum(2,3) == 5

def test_negative_sum():
    assert sum(-2, -3) == -5

# assert compara el resultado real con el esperado
# si pasa, no muestra nada
# si falla, muestra el error