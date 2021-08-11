from framework.api.http import ApiClient


def create_bug(data: dict = None, expected_code: int = 200):
    """
    :param data: data to create bug
    :param expected_code: response.status_code
    :return: requests.Response
    """
    url = "http://sheltered-atoll-54018.herokuapp.com/api/bug/"
    api = ApiClient()

    response = api.post(url=url, json=data, expected_code=expected_code)
    return response


def get_bug(expected_code: int = 200):
    """
    :param expected_code: response.status_code
    :return: requests.Response
    """
    url = "http://sheltered-atoll-54018.herokuapp.com/api/bug"
    api = ApiClient()
    response = api.get(url=url, expected_code=expected_code)
    return response


