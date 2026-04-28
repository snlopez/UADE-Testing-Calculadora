import pytest

from app.calculator import add, divide, multiply, subtract


def test_add():
    # Verifica la suma.
    assert add(2, 3) == 5


def test_subtract():
    # Verifica la resta.
    assert subtract(5, 3) == 2


def test_multiply():
    # Verifica la multiplicación.
    assert multiply(4, 3) == 12


def test_divide():
    # Verifica la división.
    assert divide(10, 2) == 5


def test_divide_by_zero():
    # Verifica que no se permita dividir por cero.
    with pytest.raises(ValueError):
        divide(10, 0)


def test_add_zero_edge_case():
    # Verifica un caso borde con cero.
    assert add(0, 0) == 0
