import logging
import sys
from base_page import BasePage
from locators import MainPageLocators, OperatorsPageLocators

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))


class OperatorsPage(BasePage):
    def click_sqrt_of_number(self):
        """Click on SQRT button."""
        logger.info("get sqrt of the number")
        self.driver.find_element(*OperatorsPageLocators.SQRT).click()

    def go_to_main_calculate_page(self):
        logger.info("close second operators menu")
        to_tap = self.driver.find_element(*MainPageLocators.X3)
        to_drag_to = self.driver.find_element(*MainPageLocators.X4)
        self.driver.scroll(to_tap, to_drag_to)

    def click_sin_of_number(self):
        logger.info("click on SIN")
        self.driver.find_element(*OperatorsPageLocators.SIN).click()

    def choose_angle(self, how, what):
        logger.info("choose angle")
        self.driver.find_element(*OperatorsPageLocators.ANGLE).click()
        self.driver.find_element(how, what).click()
