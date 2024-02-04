import pytest
from math_utils import MathUtils  # Assuming your MathUtils class is in a file named math_utils.py

# Test add method
def test_add():
    result = MathUtils.add(3, 5)
    assert result == 8

# Test subtract method
def test_subtract():
    result = MathUtils.subtract(10, 4)
    assert result == 6

# Test multiply method
def test_multiply():
    result = MathUtils.multiply(2, 7)
    assert result == 14

# Test divide method
def test_divide():
    result = MathUtils.divide(15, 3)
    assert result == 5.0

# Test divide method with division by zero
def test_divide_by_zero():
    result = MathUtils.divide(10, 0)
    assert result == -1.0