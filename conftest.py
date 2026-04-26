import pytest

from app.calculator import BaseCalculator

SUPPORTED_CALCULATOR_MODES = ("simple", "super")


def pytest_addoption(parser):
    """Register custom CLI options for this test suite."""
    parser.addoption(
        "--mode",
        action="store",
        default="simple",
        choices=SUPPORTED_CALCULATOR_MODES,
        help="calculator mode to test: simple or super",
    )


@pytest.fixture(scope="session")
def mode(request):
    """Return the selected calculator mode from CLI options."""
    return request.config.getoption("--mode")


@pytest.fixture(scope="session")
def calculator(mode):
    """Create one calculator instance per test session."""
    print(f"\n[Setup] Creating {mode} calculator")
    calculator_instance = BaseCalculator.factory(calculator_type=mode)
    yield calculator_instance

    print("\n[Teardown] Cleaning up calculator")


@pytest.fixture
def input_data():
    """Return commonly reused values for arithmetic test cases."""
    return {
        "positive": (10, 5),
        "negative": (-10, -5),
        "mixed": (-10, 5),
        "zero": (0, 0),
        "float": (10.5, 0.5),
    }


@pytest.fixture(scope="session", autouse=True)
def suite_monitor():
    """Print a lightweight banner around the test suite lifecycle."""
    print("\n>>> STARTING TEST SUITE <<<")
    yield
    print("\n>>> FINISHED TEST SUITE <<<")
