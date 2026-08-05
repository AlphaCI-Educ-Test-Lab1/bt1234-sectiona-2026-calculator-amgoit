import pytest

from src.calculator import add, divide, multiply, subtract


def test_adds_two_numbers():
    assert add(2, 2) == 4


@pytest.mark.skip(reason="TODO: implement subtract")
def test_subtracts_two_numbers():
    assert subtract(10, 7) == 3


@pytest.mark.skip(reason="TODO: implement multiply")
def test_multiplies_two_numbers():
    assert multiply(6, 7) == 42


@pytest.mark.skip(reason="TODO: implement divide")
def test_divides_two_numbers():
    assert divide(9, 3) == 3


@pytest.mark.skip(reason="TODO: implement divide")
def test_refuses_to_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)
