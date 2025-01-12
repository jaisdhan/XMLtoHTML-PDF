import pytest

def divide(a,b):
    if b == 0:
        raise ValueError("Cannot be divided by 0")
    return a/b

def test_correct_division():
    assert divide(10, 2) == 5

def test_division_cero():
    with pytest.raises(ValueError, match="Cannot be divided by 0"):
        assert divide(10,0)

# pytest.raises verifica que se lanza la expresion correcta
# match confirma que el mensaje es el error correcto
