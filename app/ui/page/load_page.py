from framework.ui.base_page import BasePage
from framework.asserts.asserts import assert_equal


class LoadPage(BasePage):

    def should_be_login_url(self):
        self.logger.debug(f'Checking if page is opened')
        load_url = self.browser.current_url
        assert_equal(load_url, "http://sheltered-atoll-54018.herokuapp.com/", "Load Url in not right")
