from framework.logger import Logger


class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.logger = Logger.get_logger()

    def open(self):
        self.logger.debug(f'Checking if page is opened')
        self.browser.get(self.url)

    def switch_to_next_window(self):
        window_after = self.browser.get_all_windows()
        self.browser.switch_to_window(window_after[1])
        self.logger.debug('Switched to the next window')


