import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))


class BasePage:
    def __init__(self, driver):
        """Start driver for testing."""
        self.driver = driver
