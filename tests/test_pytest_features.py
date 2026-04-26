import pytest
import sys


# --- 1. PARAMETRIZE (Running multiple inputs) ---
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (3, 5, 8),
        (2, 4, 6),
        (100, 200, 300),
    ],
)
def test_add_parametrized(calculator, a, b, expected):
    """
    Runs the same test 3 times with different values.
    """
    assert calculator.add(a, b) == expected


# --- 2. EXCEPTION HANDLING (pytest.raises) ---
def test_divide_by_zero(calculator):
    """
    Verifies that the code correctly crashes when dividing by zero.
    """
    with pytest.raises(ValueError) as excinfo:
        calculator.divide(10, 0)
    assert "Cannot divide by zero" in str(excinfo.value)


# --- 3. DYNAMIC SKIP (Skip inside test) ---
@pytest.mark.smoke
def test_power_feature(calculator):
    """
    Uses 'pytest.skip' dynamically if the mode is simple.
    """
    if calculator.Type == "simple":
        pytest.skip("Power is not supported in simple mode")

    assert calculator.power(2, 3) == 8


@pytest.mark.smoke
def test_sqrt_feature(calculator):
    """
    Uses 'pytest.skip' dynamically if the mode is simple.
    """
    if calculator.Type == "simple":
        pytest.skip("Sqrt is not supported in simple mode")

    assert calculator.sqrt(9) == 3.0


# --- 4. CONDITIONAL SKIP (Mark.skipif) ---
@pytest.mark.skipif(sys.platform == "win32", reason="Does not run on Windows")
def test_linux_specific_logic():
    """
    This test is skipped automatically before running if OS is Windows.
    """
    assert True


# --- 5. HARD SKIP (Mark.skip) ---
@pytest.mark.smoke
@pytest.mark.skip(reason="Feature is defined but not implemented yet")
def test_log_feature(calculator):
    """
    This test is always skipped.
    """
    calculator.log(10)


# --- 6. XFAIL (Expected Failure) ---
@pytest.mark.smoke
@pytest.mark.xfail(reason="Known Bug: Modulo calculates addition instead of remainder")
def test_modulo_bug(calculator):
    """
    We expect this to fail. If it fails, the test suite is Green.
    If it accidentally passes, Pytest will warn us (XPASS).
    """
    assert calculator.modulo(10, 3) == 1
