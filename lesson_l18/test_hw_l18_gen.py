import logging
import pathlib

from assertpy import assert_that
from logging import config

from lesson_l18.decorators import setup_teardown_decorator

path_to_project = pathlib.Path(f"{pathlib.Path.home()}/Projects/AQA_course/")

logging.config.fileConfig(f"{path_to_project}/logging_config.ini")
logging.getLogger('sampleLogger')

def pair_number_generator(num) -> list:
    return [item for item in range(0, num+1) if item % 2 == 0]

def fibonacci_generator(max_num) -> list:
    fib_range: list[int] = [0, 1]
    for item in range(2, max_num):
        fib_range.append(fib_range[item-2] + fib_range[item-1])
        if fib_range[item] > max_num:
            fib_range.pop(-1)
            break
    return fib_range


class TestSuiteGenerator:
    @setup_teardown_decorator
    def test_gen_with_even_number(self):
        logging.info(f"Set test data: even number.")
        set_number = 22
        logging.info(f"Set expected result: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]")
        expected_result = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
        logging.info("Verify expected result")
        assert_that(pair_number_generator(set_number)).is_equal_to(expected_result)

    @setup_teardown_decorator
    def test_gen_with_odd_number(self):
        logging.info(f"Set test data: even number.")
        set_number = 21
        logging.info(f"Set expected result: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]")
        expected_result = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
        logging.info("Verify expected result")
        assert_that(pair_number_generator(set_number)).is_equal_to(expected_result)



class TestSuitFibonacci:
    @setup_teardown_decorator
    def test_fibonacci_generator(self):
        logging.info(f"Set test data: maximum number in the Fabonacci array.")
        set_number = 44
        logging.info(f"Set expected result: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]")
        expected_result = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        logging.info("Verify expected result")
        assert_that(fibonacci_generator(set_number)).is_equal_to(expected_result)

    @setup_teardown_decorator
    def test_fibonacci_generator_equal(self):
        logging.info(f"Set test data: maximum number in the Fabonacci array.")
        set_number = 55
        logging.info(f"Set expected result: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]")
        expected_result = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        logging.info("Verify expected result")
        assert_that(fibonacci_generator(set_number)).is_equal_to(expected_result)
