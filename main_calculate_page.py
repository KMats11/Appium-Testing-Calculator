import logging
import sys
from base_page import BasePage
from locators import MainPageLocators

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))


class MainCalculatePage(BasePage):

    def click_on_number(self, how, what):
        logger.info("click on first number")
        self.driver.find_element(how, what).click()

    def click_on_operator(self, how, what):
        logger.info("click on operator")
        self.driver.find_element(how, what).click()

    def click_on_equal(self):
        logger.info("click on '='")
        self.driver.find_element(*MainPageLocators.EQUAL).click()

    def delete_numbers(self):
        logger.info("click on delete")
        self.driver.find_element(*MainPageLocators.DELETE).click()

    def should_be_correct_integer_result(self, operator_name):
        logger.info("get result text")
        result = float(self.driver.find_element(*MainPageLocators.RESULT).text)
        ops = {'plus': lambda x, y: x + y,
               'minus': lambda x, y: x - y,
               'divide': lambda x, y: x / y,
               'times': lambda x, y: x * y, }
        expected = float(ops[f"{operator_name}"](9, 3))
        assert result == expected, f"Expected result: {expected}, Actual result: {result}"

    def should_be_empty_result_field(self):
        logger.info("get result text")
        result = self.driver.find_element(*MainPageLocators.RESULT).text
        assert result == '', f"Expected result: empty field, Actual result: {result}"

    def should_be_correct_sqrt_result(self):
        logger.info("get result text")
        result = int(self.driver.find_element(*MainPageLocators.RESULT).text)
        square_root = 5
        assert result == square_root, f"Expected result: {square_root}, Actual result: {result}"

    def go_to_operators_page(self):
        logger.info("open second operators menu")
        to_tap = self.driver.find_element(*MainPageLocators.X1)
        to_drag_to = self.driver.find_element(*MainPageLocators.X2)
        self.driver.scroll(to_tap, to_drag_to)

    def should_be_correct_sin_answer(self, result_num):
        logger.info("get result text")
        result = self.driver.find_element(*MainPageLocators.RESULT).text
        expected = result_num
        assert result == expected, f"Expected result: {expected}, Actual result: {result}"
