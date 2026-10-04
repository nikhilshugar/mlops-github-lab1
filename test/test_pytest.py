import pytest
from src import calculator

def test_fun1():
    assert calculator.fun1(2, 3) == 5
    assert calculator.fun1(5,0) == 5
    assert calculator.fun1 (-1, 1) == 0
    assert calculator.fun1 (-1, -1) == -2


def test_fun2():
    assert calculator.fun2(2, 3) == -1
    assert calculator.fun2(5,0) == 5
    assert calculator.fun2 (-1, 1) == -2
    assert calculator.fun2 (-1, -1) == 0

def test_fun3():
    assert calculator.fun3(2, 3) == 6
    assert calculator.fun3(5,0) == 0
    assert calculator.fun3 (-1, 1) == -1

    assert calculator.fun3 (-1, -1) == 1

def test_fun4():
    assert calculator.fun4(2, 3, 5) == 10
    assert calculator.fun4(5,0, -1) == 4
    assert calculator.fun4 (-1, -1, -1) == -3

    assert calculator.fun4 (-1, -1, 100) == 98

def test_fun4_invalid_input():
    with pytest.raises(ValueError):
        calculator.fun4(1, 2, "3")

@pytest.mark.parametrize("x, y, expected", [
    (10, 4, 2.5),
    (9, 3, 3),
    (-6, 2, -3),
    (5, -2, -2.5),
])
def test_fun5(x, y, expected):
    assert calculator.fun5(x, y) == expected

def test_fun5_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculator.fun5(5, 0)

@pytest.mark.parametrize("x, y, expected", [
    (2, 10, 1024),
    (5, 0, 1),
    (-2, 3, -8),
    (4, 0.5, 2),
])
def test_fun6(x, y, expected):
    assert calculator.fun6(x, y) == expected

# every two-input function should reject a non-number
@pytest.mark.parametrize("func", [calculator.fun1, calculator.fun2, calculator.fun3,
                                  calculator.fun5, calculator.fun6])
def test_invalid_input(func):
    with pytest.raises(ValueError):
        func("2", 3)