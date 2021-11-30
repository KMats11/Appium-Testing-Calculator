import logging
import sys
from base_page import BasePage

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))


class MainCalculatePage(BasePage):
    def click_on_number(self, how, what):
        logger.info("click on first number")
        driver.find_element(how, what).click()

        