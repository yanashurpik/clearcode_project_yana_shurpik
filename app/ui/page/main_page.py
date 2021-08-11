from framework.ui.base_page import BasePage
from framework.ui.elements import Block, TextField, Button
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    # locators
    _page_loading_locator = (By.XPATH, "//h1[text()='Bugs Manager']")
    _add_bug_title_locator = (By.XPATH, "//span[@class='card-text']/input[1]")
    _add_bug_description_locator = (By.XPATH, "//span[@class='card-text']/input[2]")
    _add_bug_button_locator = (By.XPATH, "//button[text()='Add Bug']")

    def is_page_open(self):
        page = Block(*self._page_loading_locator)
        return page.is_element_present(self.browser)

    def add_bug_title_input(self, title):
        title_locator = TextField(*self._add_bug_title_locator)
        title_locator.wait_for_element(self.browser)
        title_locator.send_text(self.browser, title)

    def add_bug_description_input(self, description):
        description_locator = TextField(*self._add_bug_description_locator)
        description_locator.wait_for_element(self.browser)
        description_locator.send_text(self.browser, description)

    def add_bug_button_click(self):
        button = Button(*self._add_bug_button_locator)
        button.click(self.browser)

    def delete_bug_button_click(self, description):
        button = Button(By.XPATH, f"//td[text()='{description}']/following-sibling::td/button")
        button.wait_for_element(self.browser)
        button.click(self.browser)

    def check_bug_in_the_table(self, title, description):
        bug_title = TextField(By.XPATH, f'//tbody[@role="rowgroup"]//td[text()="{title}"]')
        bug_title.wait_for_element(self.browser)
        bug_description = TextField(By.XPATH, f'//tbody[@role="rowgroup"]//td[text()="{description}"]')
        if bug_title.is_element_present(self.browser) and bug_description.is_element_present(self.browser):
            return True
