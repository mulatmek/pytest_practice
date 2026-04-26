import pytest

# --- Basic Smoke Tests (No special decorators) ---


@pytest.mark.smoke
def test_add_simple(calculator):
    """
    Standard test: Check if 10 + 5 equals 15.
    """
    assert calculator.add(10, 5) == 15


@pytest.mark.smoke
def test_subtract_simple(calculator):
    """
    Standard test: Check if 10 - 5 equals 5.
    """
    assert calculator.subtract(10, 5) == 5


@pytest.mark.smoke
def test_multiply_simple(calculator):
    """
    Standard test: Check if 10 * 5 equals 50.
    """
    assert calculator.multiply(10, 5) == 50


@pytest.mark.smoke
def test_divide_simple(calculator):
    """
    Standard test: Check if 10 / 2 equals 5.0.
    """
    assert calculator.divide(10, 2) == 5.0
