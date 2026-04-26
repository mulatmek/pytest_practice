import pytest


# --- Test 1: Standard Positive Integers ---
def test_add_positive_numbers(calculator, input_data):
    """
    Uses 'positive' data: (10, 5)
    Expected: 10 + 5 = 15
    """
    a, b = input_data["positive"]
    result = calculator.add(a, b)
    assert result == 15


# --- Test 2: Negative Numbers Logic ---
def test_subtract_negative_numbers(calculator, input_data):
    """
    Uses 'negative' data: (-10, -5)
    Expected: -10 - (-5) = -5
    """
    a, b = input_data["negative"]
    result = calculator.subtract(a, b)
    assert result == -5


# --- Test 3: Mixed Sign Multiplication ---
def test_multiply_mixed_signed(calculator, input_data):
    """
    Uses 'mixed' data: (-10, 5)
    Expected: -10 * 5 = -50
    """
    a, b = input_data["mixed"]
    result = calculator.multiply(a, b)
    assert result == -50


# --- Test 4: Floating Point Precision ---
def test_add_floating_points(calculator, input_data):
    """
    Uses 'float' data: (10.5, 0.5)
    Expected: 10.5 + 0.5 = 11.0
    """
    a, b = input_data["float"]
    result = calculator.add(a, b)
    assert result == 11.0


# --- Test 5: Edge Case - Division by Zero ---
def test_divide_by_zero_error(calculator, input_data):
    """
    Uses 'zero' data: (0, 0)
    Expected: ValueError (Cannot divide by zero)
    """
    a, b = input_data["zero"]

    # We expect the calculator to crash safely
    with pytest.raises(ValueError) as excinfo:
        calculator.divide(a, b)

    assert "Cannot divide by zero" in str(excinfo.value)
