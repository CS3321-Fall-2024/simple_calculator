# tests/test_simple_calculator.py
import pytest
import math
from simple_calculator.calculator import (
    squareNums,
    triNums,
    lazyCaterer,
    magicSquares,
    cubeNums,
    circNum,
    surfArea,
)

# Test for squareNums function
@pytest.mark.parametrize("n, expected", [
    (2, 4),
    (3, 9),
    (-4, 16),
])
def test_squareNums(n, expected):
    """Test squareNums function with various integers"""
    assert squareNums(n) == expected

# Test for cubeNums function
@pytest.mark.parametrize("n, expected", [
    (2, 8),
    (3, 27),
    (-4, -64),
])
def test_cubeNums(n, expected):
    """Test cubeNums function with various integers"""
    assert cubeNums(n) == expected

# Test for triNums function
@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (3, 6),
    (5, 15),
])
def test_triNums(n, expected):
    """Test triNums function with various integers"""
    assert triNums(n) == expected

# Test for lazyCaterer function
@pytest.mark.parametrize("n, expected", [
    (1, 2),
    (2, 4),
    (3, 7),
])
def test_lazyCaterer(n, expected):
    """Test lazyCaterer function with various integers"""
    assert lazyCaterer(n) == expected

# Test for magicSquares function
@pytest.mark.parametrize("n, expected", [
    (3, 15),
    (4, 34),
    (5, 65),
])
def test_magicSquares(n, expected):
    """Test magicSquares function with various integers"""
    assert magicSquares(n) == expected

# Test for circNum function
@pytest.mark.parametrize("n, expected", [
    (1, 2 * math.pi * 1),
    (2, 2 * math.pi * 2),
    (3, 2 * math.pi * 3),
])
def test_circNum(n, expected):
    """Test circNum function with various radii"""
    assert circNum(n) == pytest.approx(expected)

# Test for surfArea function
@pytest.mark.parametrize("n, expected", [
    (1, 4 * math.pi * 1**2),
    (2, 4 * math.pi * 2**2),
    (3, 4 * math.pi * 3**2),
])
def test_surfArea(n, expected):
    """Test surfArea function with various radii"""
    assert surfArea(n) == pytest.approx(expected)
