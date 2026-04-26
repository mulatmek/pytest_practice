import pytest

from app.calculator import BaseCalculator


# --- CLI Options ---
def pytest_addoption(parser):
    parser.addoption("--mode", action="store", default="simple", help="basic or super")


@pytest.fixture(scope="session")
def mode(request):
    return request.config.getoption("--mode")


@pytest.fixture(scope="session")
def calculator(mode):

    print(f"\n[Setup] Creating {mode} calculator")

    app = BaseCalculator.factory(calculator_type=mode)

    yield app

    print("\n[Teardown] Cleaning up calculator")


# --- Fixture 2: Data Provider (Returns Data) ---
@pytest.fixture
def input_data():
    """
    Returns a dictionary of interesting numbers to test with.
    """
    return {
        "positive": (10, 5),
        "negative": (-10, -5),
        "mixed": (-10, 5),
        "zero": (0, 0),
        "float": (10.5, 0.5),
    }


@pytest.fixture(scope="session", autouse=True)
def suite_monitor():
    print("\n>>> STARTING TEST SUITE <<<")

    yield

    print("\n>>> FINISHED TEST SUITE <<<")
