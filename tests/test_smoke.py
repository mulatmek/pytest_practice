import pytest

@pytest.mark.smoke
@pytest.mark.parametrize(
    ("operation", "left", "right", "expected"),
    [
        ("add", 10, 5, 15),
        ("subtract", 10, 5, 5),
        ("multiply", 10, 5, 50),
        ("divide", 10, 2, 5.0),
    ],
    ids=["add", "subtract", "multiply", "divide"],
)
def test_basic_operations_smoke(calculator, operation, left, right, expected):
    """Validate core arithmetic operations with representative inputs."""
    operation_method = getattr(calculator, operation)
    assert operation_method(left, right) == expected
