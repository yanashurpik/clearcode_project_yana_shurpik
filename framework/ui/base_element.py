from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

from framework.logger import Logger


class BaseElement:
    def __init__(self, by_type, locator, element=None):
        self.by_type = by_type
        self.locator = locator
        if element:
            self.element = element
        else:
            self.element = None
        self.logger = Logger.get_logger()
        self.logger.debug(f"{self.__class__.__name__}: Element was created")

    def is_element_present(self, browser):
        try:
            browser.find_element(self.by_type, self.locator)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, browser, timeout=4):
        try:
            WebDriverWait(browser, timeout).until(ec.presence_of_element_located((self.by_type, self.locator)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, browser, timeout=4):
        try:
            WebDriverWait(browser, timeout, 1, TimeoutException). \
                until_not(ec.presence_of_element_located((self.by_type, self.locator)))
        except TimeoutException:
            print("TimeoutException")
        return True

    def wait_for_element(self, browser):
        wait_sec = 5
        try:
            WebDriverWait(browser, wait_sec,
                          ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                              ElementNotSelectableException]) \
                .until(ec.element_to_be_clickable((self.by_type, self.locator)))
        except TimeoutException:
            self.logger.debug("TimeoutException")

    def get_element(self, browser):
        if self.element is None:
            self.element = browser.find_element(self.by_type, self.locator)
        return self.element

    def click(self, browser):
        self.get_element(browser)
        self.logger.debug(f"Click on element: {self.by_type, self.locator}")
        self.element.click()

    def send_text(self, browser, text: str):
        self.get_element(browser)
        self.logger.debug(f"Send text: {text} to element: {self.by_type, self.locator}")
        self.element.send_keys(text)

    def send_keys(self, browser, key):
        self.get_element(browser)
        self.logger.debug(f"Send keys: {key} to element: {self.by_type, self.locator}")
        self.element.send_keys(key)
