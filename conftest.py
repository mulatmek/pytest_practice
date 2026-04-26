from pathlib import Path

import pytest

from app.calculator import BaseCalculator
from utils.logging_utils import configure_test_logging, shutdown_logger

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


@pytest.fixture(scope="session", autouse=True)
def configure_framework_logging():
    """Initialize framework logging one time for the test session."""
    logger, log_file = configure_test_logging(Path(__file__).resolve().parent)
    logger.warning("Framework logging initialized. file=%s", log_file)
    yield logger

    logger.warning("Framework logging shutdown")
    shutdown_logger(logger)


@pytest.fixture(scope="session")
def calculator(mode, configure_framework_logging):
    """Create one calculator instance per test session."""
    logger = configure_framework_logging
    logger.info("[Setup] Creating %s calculator", mode)
    logger.debug("Creating calculator through BaseCalculator.factory")
    calculator_instance = BaseCalculator.factory(calculator_type=mode)
    yield calculator_instance

    logger.info("[Teardown] Cleaning up calculator")


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
def suite_monitor(configure_framework_logging):
    """Log a lightweight banner around the test suite lifecycle."""
    logger = configure_framework_logging
    logger.info(">>> STARTING TEST SUITE <<<")
    yield
    logger.info(">>> FINISHED TEST SUITE <<<")
