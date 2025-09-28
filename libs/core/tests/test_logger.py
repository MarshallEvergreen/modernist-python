"""Test for the core library."""

from core import logger


class TestLogger:
    def test_sanity(self) -> None:
        assert logger is not None
