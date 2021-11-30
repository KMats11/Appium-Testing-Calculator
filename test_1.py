import sys
import pytest
import logging
from locators import MainPageLocators, OperatorsPageLocators
from appium.webdriver.common.mobileby import By
from main_calculate_page import MainCalculatePage

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))


@pytest.mark.parametrize('operator_text', ["divide", "times", "minus", "plus"])
def test_sum_of_two_integers(driver, operator_text):
    """Check operators of two numbers"""
    MainCalculatePage.click_on_number()
    logger.info("click on operator")
    driver.find_element(By.XPATH, f"//android.widget.Button[@content-desc='{operator_text}']").click()
    logger.info("click on second number")
    driver.find_element(*MainPageLocators.THREE).click()  # Позиционировать с элементами ID до 9
    logger.info("click on '='")
    driver.find_element(*MainPageLocators.EQUAL).click()
    logger.info("get result")
    result = float(driver.find_element(*MainPageLocators.RESULT).text)
    ops = {'plus': lambda x, y: x + y,
           'minus': lambda x, y: x - y,
           'divide': lambda x, y: x / y,
           'times': lambda x, y: x * y, }
    expected = float(ops[f"{operator_text}"](9, 3))
    assert result == expected, f"Expected result: {expected}, Actual result: {result}"


def test_delete_number(driver):
    """Check of deleting number"""
    logger.info("click on number")
    driver.find_element(*MainPageLocators.THREE).click()
    logger.info("click on delete")
    driver.find_element(*MainPageLocators.DELETE).click()
    logger.info("get result text")
    result = driver.find_element(*MainPageLocators.RESULT).text
    assert result == '', f"Expected result: {result}, Actual result: {None}"


def test_root_of_number(driver):
    """Check square root of number"""
    logger.info("open second operators menu")
    to_tap = driver.find_element(*MainPageLocators.X1)
    to_drag_to = driver.find_element(*MainPageLocators.X2)
    driver.scroll(to_tap, to_drag_to)

    driver.find_element(*OperatorsPageLocators.SQRT).click()
    logger.info("close second operators menu")
    to_tap = driver.find_element(*MainPageLocators.X3)
    to_drag_to = driver.find_element(*MainPageLocators.X4)
    driver.scroll(to_tap, to_drag_to)

    logger.info("enter number to calculate")
    driver.find_element(*MainPageLocators.TWO).click()
    driver.find_element(*MainPageLocators.FIVE).click()
    driver.find_element(*MainPageLocators.EQUAL).click()

    logger.info("get result text")
    result = int(driver.find_element(*MainPageLocators.RESULT).text)
    square_root = 5
    assert result == square_root, f"Expected result: {square_root}, Actual result: {result}"


@pytest.mark.parametrize('how, what, result_num', [(*OperatorsPageLocators.RADIAN, "−0.9880316"),
                                               (*OperatorsPageLocators.DEGREE, "0.5")])
def test_sin(driver, how, what, result_num):
    """Check sin of angle"""
    logger.info("open second operators menu")
    to_tap = driver.find_element(*MainPageLocators.X1)
    to_drag_to = driver.find_element(*MainPageLocators.X2)
    driver.scroll(to_tap, to_drag_to)
    logger.info("click on SIN")
    driver.find_element(*OperatorsPageLocators.SIN).click()
    logger.info("choose angle")
    driver.find_element(*OperatorsPageLocators.ANGLE).click()
    driver.find_element(how, what).click()
    logger.info("close second operators menu")
    to_tap = driver.find_element(*MainPageLocators.X3)
    to_drag_to = driver.find_element(*MainPageLocators.X4)
    driver.scroll(to_tap, to_drag_to)

    logger.info("enter angle to calculate SIN")
    # wait
    driver.find_element(*MainPageLocators.THREE).click()
    driver.find_element(*MainPageLocators.ZERO).click()
    driver.find_element(*MainPageLocators.EQUAL).click()

    logger.info("get result text")
    result = driver.find_element(*MainPageLocators.RESULT).text
    expected = result_num
    assert result == expected, f"Expected result: {expected}, Actual result: {result}"
