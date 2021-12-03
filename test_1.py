import sys
import allure
import pytest
import logging
from locators import MainPageLocators, OperatorsPageLocators
from main_calculate_page import MainCalculatePage
from operators_page import OperatorsPage

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))


@allure.title('Verify that basic operators calculates correctly for integer numbers')
@pytest.mark.parametrize('operator_locator, operator_name', [(MainPageLocators.DIVIDE, 'divide'),
                                                             (MainPageLocators.TIMES, 'times'),
                                                             (MainPageLocators.MINUS, 'minus'),
                                                             (MainPageLocators.PLUS, 'plus')])
def test_of_two_integers(driver, operator_locator, operator_name):
    """Check operators of two numbers"""
    calculator = MainCalculatePage(driver)
    calculator.click_on_number(*MainPageLocators.NINE)
    calculator.click_on_operator(*operator_locator)
    calculator.click_on_number(*MainPageLocators.THREE)
    calculator.click_on_equal()
    calculator.should_be_correct_integer_result(operator_name)


@allure.title('Verify that number can be deleted')
def test_delete_number(driver):
    """Check of deleting number"""
    calculator = MainCalculatePage(driver)
    calculator.click_on_number(*MainPageLocators.THREE)
    calculator.delete_numbers()
    calculator.should_be_empty_result_field()


@allure.title('Verify that square root of integer number calculates correctly')
def test_root_of_number(driver):
    """Check square root of number"""
    calculator = MainCalculatePage(driver)
    calculator.go_to_operators_page()

    operators_page = OperatorsPage(driver)
    operators_page.click_sqrt_of_number()
    operators_page.go_to_main_calculate_page()

    calculator = MainCalculatePage(driver)
    calculator.click_on_number(*MainPageLocators.TWO)
    calculator.click_on_number(*MainPageLocators.FIVE)
    calculator.click_on_equal()
    calculator.should_be_correct_sqrt_result()


@allure.title('Verify that function sin of number calculates correctly')
@pytest.mark.parametrize('how, what, result_num', [(*OperatorsPageLocators.RADIAN, "−0.9880316"),
                                                   (*OperatorsPageLocators.DEGREE, "0.5")])
def test_sin(driver, how, what, result_num):
    """Check sin of angle"""

    calculator = MainCalculatePage(driver)
    calculator.go_to_operators_page()

    operators_page = OperatorsPage(driver)
    operators_page.click_sin_of_number()
    operators_page.choose_angle(how, what)
    operators_page.go_to_main_calculate_page()

    calculator = MainCalculatePage(driver)
    # wait
    calculator.click_on_number(*MainPageLocators.THREE)
    calculator.click_on_number(*MainPageLocators.ZERO)
    calculator.click_on_equal()

    calculator.should_be_correct_sin_answer(result_num)

# pytest --alluredir=/tmp/my_allure_results
# allure serve /tmp/my_allure_results
