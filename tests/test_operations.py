import pytest
from calculator.operations import add, subtract, multiply, divide


@pytest.mark.parametrize("a, b, expected", [(5, 3, 8), (-1, 1, 0), (2.5, 2.5, 5.0)])
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(10, 4, 6), (0, 5, -5)])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(3, 4, 12), (-2, 3, -6)])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(20, 5, 4), (7, 2, 3.5)])
def test_divide(a, b, expected):
    assert divide(a, b) == expected


def test_divide_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        divide(10, 0)
