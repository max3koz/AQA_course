import logging
from logging import config

from assertpy import assert_that
from lesson_15.rhombus import Rhombus

logging.config.fileConfig('logging_config.ini')
logging.getLogger('sampleLogger')

class TestSuite:

    def test_verify_that_catch_exception_with_side_negative_value(self):
        logging.info("")
        logging.info(f"Step 1: Set test suite data with negative value of rhombus side")
        negative_side_value = -50
        negative_angle_value = 60
        logging.info(f"Step 2: Set the expected exception message with invalid side value {negative_side_value}")
        expected_result = (f"The length of rhombus side must be positive number! You entered negative number: "
                           f"{negative_side_value}.")
        logging.info(f"Step 3: Get the result of test case.")
        try:
            Rhombus(negative_side_value, negative_angle_value)
        except ValueError as exception:
            assert_that(exception.args[0]).is_equal_to(expected_result)


    def test_verify_that_catch_exception_with_angle_negative_value(self):
        logging.info("")
        logging.info(f"Step 1: Set test suite data with negative value of rhombus angle")
        negative_side_value = 50
        negative_angle_value = -50
        logging.info(f"Step 2: Set the expected exception message with invalid angle value {negative_angle_value}")
        expected_result = (f"The length of rhombus angle_a must be from 1 till 179! You entered negative number: "
                           f"{negative_angle_value}.")
        logging.info(f"Step 3: Get the result of test case.")
        try:
            Rhombus(negative_side_value, negative_angle_value)
        except ValueError as exception:
            assert_that(exception.args[0]).is_equal_to(expected_result)

    def test_verify_that_all_rhombus_values_set(self):
        logging.info("")
        logging.info(f"Step 1: Set test suite data with valid value of rhombus")
        side_value = 50
        angle_value = 60
        rhombus_1 = Rhombus(side_value, angle_value)
        logging.info(f"Step 2: Get the value of the rhombus side.")
        assert_that(rhombus_1.side).is_equal_to(side_value)
        logging.info(f"Step 3: Get the result of the rhombus angle a.")
        assert_that(rhombus_1.angle_a).is_equal_to(angle_value)
        logging.info(f"Step 4: Get the result of the rhombus angle b.")
        assert_that(rhombus_1.angle_b).is_equal_to(180 - angle_value)

