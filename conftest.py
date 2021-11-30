import sys
import pytest
import logging
from appium import webdriver

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))


@pytest.fixture(scope="function")
def driver():
    """start driver for each test"""
    desired_caps = {
        "platformName": "Android",
        "appium:deviceName": "AndroidTestDevice",
        "appium:platformVersion": "10.0",
        "appium:appPackage": "com.dalviksoft.calculator",
        "appium:appActivity": "com.android2.calculator3.Calculator"
    }

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    logger.info('start driver for test')

    yield driver
    logger.info('quit driver')
    driver.quit()
