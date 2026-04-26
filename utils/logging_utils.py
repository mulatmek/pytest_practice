import logging
import sys
from datetime import datetime
from pathlib import Path

LOGGER_NAME = "pytest_framework"


def configure_test_logging(base_dir: Path) -> tuple[logging.Logger, Path]:
    """Configure framework logging with file and stdout handlers."""
    logger = logging.getLogger(LOGGER_NAME)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    log_dir = base_dir / "logs"
    log_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = log_dir / f"test_run_{timestamp}.log"

    formatter = logging.Formatter(
        fmt=(
            "%(asctime)s.%(msecs)03d | %(levelname)-8s | %(name)s | "
            "%(filename)s:%(lineno)d | %(message)s"
        ),
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.WARNING)
    stdout_handler.setFormatter(formatter)

    logger.handlers.clear()
    logger.addHandler(file_handler)
    logger.addHandler(stdout_handler)

    return logger, log_file


def shutdown_logger(logger: logging.Logger) -> None:
    """Close and clear all logger handlers."""
    for handler in logger.handlers:
        handler.close()
    logger.handlers.clear()
