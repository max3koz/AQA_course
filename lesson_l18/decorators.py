import logging

from assertpy import assert_that


def setup_teardown_decorator(func):
    def wrapper(*args):
        logging.info("Logging is starting!")
        logging.info(f"Test {func.__name__}  is running with the argument {args}!")
        try:
            result = func(args)
            logging.info(f"Test {func.__name__} was finished with the expected result.")
            return result
        except Exception as exception:
            logging.error(f"Test {func.__name__} was finished with {exception}.")
            assert False
    return wrapper
