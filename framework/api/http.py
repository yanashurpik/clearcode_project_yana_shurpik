import time
from framework.logger import Logger
from framework.asserts.asserts import assert_equal
from .request_timeout import RequestTimeout
from framework.utils import get_value_by_key
from json import JSONDecodeError
from requests.exceptions import ConnectionError
import requests


class ApiClient:

    @RequestTimeout.request_timer()
    def post(self, url=None, params=None, data=None, json=None, headers=None, expected_code: int = 200):
        logger = Logger.get_logger()
        try:
            response = requests.post(url=url, params=params, data=data, json=json, headers=headers)
            logger.api(response=response)
            try:
                if get_value_by_key('error', response.json()) == ['Too Many Attempts.']:
                    time.sleep(3)
                    response = requests.post(url=url, data=data, json=json, expected_code=expected_code)
                else:
                    assert_equal(response.status_code, expected_code,
                                 f"Status code: {response.status_code} isn\'t equal expected code: {expected_code}")
            except JSONDecodeError:
                logger.debug("Http request without json in response")
            return response
        except ConnectionError as err:
            logger.error(err)
            requests.post(url=url, data=data, json=json, expected_code=expected_code)

    @RequestTimeout.request_timer()
    def get(self, url=None, params=None, headers=None, expected_code: int = 200):
        logger = Logger.get_logger()
        try:
            response = requests.get(url=url, params=params, headers=headers)
            logger.api(response=response)
            try:
                if get_value_by_key('error', response.json()) == ['Too Many Attempts.']:
                    time.sleep(3)
                    response = requests.get(url=url, params=params, expected_code=expected_code)
                elif 'file_put_contents' in str(get_value_by_key('error', response.json())):
                    logger.debug(f"Status code: {response.status_code}, error: 'file_put_contents'")
                else:
                    assert_equal(response.status_code, expected_code,
                                 f"Status code: {response.status_code} isn\'t equal expected code: {expected_code}")
            except JSONDecodeError:
                logger.debug("Http request without json in response")
            return response
        except ConnectionError as err:
            logger.error(err)
            requests.get(url=url, params=params, expected_code=expected_code)

    @RequestTimeout.request_timer()
    def delete(self, url=None, params=None, expected_code: int = 200):
        logger = Logger.get_logger()
        response = requests.delete(url=url, params=params)
        logger.api(response=response)
        try:
            if get_value_by_key('error', response.json()) == ['Too Many Attempts.']:
                time.sleep(1)
                response = requests.delete(url=url, params=params, expected_code=expected_code)
            else:
                assert_equal(response.status_code, expected_code,
                             f"Status code: {response.status_code} isn\'t equal expected code: {expected_code}")
        except JSONDecodeError:
            logger.debug("Http request without json in response")
        return response
