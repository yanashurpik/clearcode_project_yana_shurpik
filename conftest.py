import pytest
from app.ui.page.load_page import LoadPage
from selenium.webdriver.chrome.options import Options
from framework.logger import Logger
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Choose language")


@pytest.fixture(scope="session")
def browser(request):

    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="session")
def setup(browser):
    link = "http://sheltered-atoll.herokuapp.com/"
    page = LoadPage(browser, link)
    page.open()


@pytest.fixture(scope='session')
def logger():
    logger = Logger.get_logger()
    return logger
