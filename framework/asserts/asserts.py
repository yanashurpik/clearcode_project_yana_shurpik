from framework.logger import Logger


def assert_equal(left_part, right_part, message):
    logger = Logger.get_logger()
    try:
        assert left_part == right_part, message
    except AssertionError as err:
        logger.error(message)
        raise err


def assert_true(expression, message):
    logger = Logger.get_logger()
    try:
        assert expression, message
    except AssertionError as err:
        logger.error(message)
        raise err


def assert_false(expression, message, soft_assert=False):
    logger = Logger.get_logger()
    try:
        assert not expression, message
    except AssertionError as err:
        logger.error(message)
        if not soft_assert:
            raise err
