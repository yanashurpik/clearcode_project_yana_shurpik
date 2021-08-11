import pytest

from app.api.bugs import *
from tests.test_data.data import data_to_create_bug_api
from framework.asserts.asserts import assert_equal, assert_true


@pytest.mark.api
def test_add_bug_api(logger):
    logger.test_name(test_name="Test Add Bug API")

    logger.step(step_desc="Create bug")
    r = create_bug(data_to_create_bug_api)
    assert_equal(r.status_code, 200, f"Wrong status code {r.status_code}")

    logger.step(step_desc="Get all bugs and check bug added")
    r = get_bug()
    is_bug_in_table = False
    for i in r.json():
        if i["title"] == data_to_create_bug_api["title"] and i["description"] == data_to_create_bug_api["description"]:
            is_bug_in_table = True
    assert_true(is_bug_in_table, "Bug is not in table")
