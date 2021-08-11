from app.ui.page.main_page import MainPage
import pytest
from framework.asserts.asserts import assert_true
from tests.test_data.data import valid_title, valid_description


@pytest.mark.ui
def test_add_delete_bug(setup, browser, logger):
    logger.test_name(browser_name=browser.name)

    logger.step(step_desc="Open Bug Manager Page")
    main_page = MainPage(browser, browser.current_url)
    assert_true(main_page.is_page_open(), "Page is not open")

    logger.step(step_desc="Fill in the fields title and description")

    main_page.add_bug_title_input(valid_title)
    main_page.add_bug_description_input(valid_description)

    logger.step(step_desc="Click on Add bug button")
    main_page.add_bug_button_click()

    logger.step(step_desc="Check new bug added")
    assert_true(main_page.check_bug_in_the_table(valid_title, valid_description), "Bug was not added")









