from app.calculations import add, subtract, multiply, divide
import pytest

@pytest.mark.parametrize("num1, num2, sum", [(3,2,5), (7,1,8), (2,4,6)])
def test_add(num1, num2, sum):
    assert add(num1,num2) == sum 

def test_subtract():
    assert subtract(9, 4) == 5


def test_multiply():
    assert multiply(4, 3) == 12


def test_divde():
    assert divide(20, 5) == 4