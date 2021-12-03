import logging
import sys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import allure

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))


class BasePage:
    def __init__(self, driver):
        """Start driver for testing."""
        self.driver = driver

    def is_element_present(self, how, what):
        """Check is there an element on the page.

        Keyword arguments:
        how -- method to find an element
        what -- locator of an element on the page"""
        with allure.step("Check is element present on the page"):
            try:
                logger.info(f"Check is element {what} present on the page")
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((how, what))
                )
                self.driver.find_element(how, what)
            except NoSuchElementException:
                return False
            return True
