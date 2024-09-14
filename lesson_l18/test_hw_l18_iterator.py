import logging
import pathlib

from assertpy import assert_that
from logging import config

from lesson_l18.decorators import setup_teardown_decorator

path_to_project = pathlib.Path(f"{pathlib.Path.home()}/Projects/AQA_course/")

logging.config.fileConfig(f"{path_to_project}/logging_config.ini")
logging.getLogger('sampleLogger')

def revers_list(execute_list):
    return execute_list[::-1]

def revers_iter(execute_list):
    my_iter = iter(execute_list[::-1])
    return my_iter

def iterable_pair_number(num):
     pair_number_iterator = iter(item for item in range(0, num+1) if item % 2 == 0)
     return pair_number_iterator

print(iterable_pair_number(10))

class TestSuiteIteratorRevers:
    @setup_teardown_decorator
    def test_revers_list_by_iterator(self):
        logging.info(f"Set test data: the array [0, 1, 2].")
        sample_list = [0, 1, 2]
        logging.info(f"Set expected result: [2, 1, 0]")
        expected_result = revers_list(sample_list)
        logging.info("Verify expected result")
        iterable = revers_iter(sample_list)
        for index in range(len(sample_list)):
            assert_that(next(iterable)).is_equal_to(expected_result[index])

class TestSuiteIteratorPairNumber:
    @setup_teardown_decorator
    def test_pair_number_even(self):
        logging.info(f"Set test data: the even number 10.")
        sample_number = 10
        logging.info(f"Set expected result: [0, 2, 4, 6, 8, 10]")
        expected_result = [0, 2, 4, 6, 8, 10]
        logging.info("Verify expected result")
        iterable = iterable_pair_number(sample_number)
        count = 0
        for next_num in iterable:
            assert_that(next_num).is_equal_to(expected_result[count])
            count += 1

    @setup_teardown_decorator
    def test_pair_number_odd(self):
        logging.info(f"Set test data: the odd number 9.")
        sample_number = 9
        logging.info(f"Set expected result: [0, 2, 4, 6, 8]")
        expected_result = [0, 2, 4, 6, 8]
        logging.info("Verify expected result")
        iterable = iterable_pair_number(sample_number)
        count = 0
        for next_num in iterable:
            assert_that(next_num).is_equal_to(expected_result[count])
            count += 1
