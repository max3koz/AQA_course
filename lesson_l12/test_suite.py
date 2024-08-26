import logging

from assertpy import assert_that, fail
from logging import config

from lesson_l12.lesson12_function_for_test import (cal_adv_value_man_height, concatenate_strings, change_char_in_string,
                                                   check_on_palindrom, word_count)


logging.config.fileConfig('logging_config.ini')
logging.getLogger('sampleLogger')

print(check_on_palindrom("ass"))

class TestSuitTask02:

    def test_case_with_not_empty_srting(self):
        logging.info("Step 1: Set string with 2 word")
        test_text = "The mother wishes the window."
        logging.info("Step 2: Verify that the sentence have 5 words")
        assert_that(word_count(test_text)).is_equal_to(5)

    def test_case_with_empty_srting(self):
        logging.info("Step 1: Set string with 2 word")
        test_text = ""
        logging.info("Step 2: Verify that the sentence is empty")
        assert_that(word_count(test_text)).is_equal_to(0)

class TestSuitTask03:

    def test_case_with_not_empty_srting_list_and_symbol(self):
        logging.info("Step 1: Set string list with 3 words and symbol \"-\"")
        test_string_list = ["asgdf", "231q5", "asdg"]
        symbol = "-"
        expected_result= "asgdf-231q5-asdg"
        logging.info("Step 2: Verify that to create the expected string with symbol \"-\"")
        assert_that(concatenate_strings(test_string_list, symbol)).is_equal_to(expected_result)

    def test_case_with_nsrting_list_and_empty_symbol(self):
        logging.info("Step 1: Set string list with 3 words and empty symbol")
        test_string_list = ["asgdf", "231q5", "asdg"]
        symbol = ""
        expected_result= "asgdf231q5asdg"
        logging.info("Step 2: Verify that to create the expected string with empty symbol")
        assert_that(concatenate_strings(test_string_list, symbol)).is_equal_to(expected_result)

    def test_case_with_empty_srting_list_and_symbol(self):
        logging.info("Step 1: Set empty string list and symbol \"-\"")
        test_string_list = []
        symbol = "-"
        expected_result= ""
        logging.info("Step 2: Verify that to create the expected string with symbol \"-\"")
        assert_that(concatenate_strings(test_string_list, symbol)).is_equal_to(expected_result)

class TestSuitTask04:

    def test_case_verify_that_upper_fun_run(self):
        logging.info("Step 1: Set the test string.")
        test_text = "The mother Washed The Window FRAME!"
        logging.info("Step 2: Verify that all chars are upper in the sentence.")
        assert_that(change_char_in_string(test_text, "upper", "")).is_equal_to(test_text.upper())

    def test_case_verify_that_lower_fun_run(self):
        logging.info("Step 1: Set the test string.")
        test_text = "The Mother Washed The Window FRAME!"
        logging.info("Step 2: Verify that all chars are lower in the sentence.")
        assert_that(change_char_in_string(test_text, "lower", "")).is_equal_to(test_text.lower())

    def test_case_verify_that_startswith_fun_run_positive(self):
        logging.info("Step 1: Set the test string.")
        test_text = "The Mother Washed The Window FRAME!"
        logging.info("Step 2: Verify that the positive case is passed for the startswith function.")
        assert_that(change_char_in_string(test_text, "startswith", "T")).is_true()

    def test_case_verify_that_startswith_fun_run_negative(self):
        logging.info("Step 1: Set the test string.")
        test_text = "The Mother Washed The Window FRAME!"
        logging.info("Step 2:Verify that the positive case is passed for the startswith function.")
        assert_that(change_char_in_string(test_text, "startswith", "t")).is_false()

    def test_case_verify_that_endswith_fun_run_positive(self):
        logging.info("Step 1: Set the test string.")
        test_text = "The Mother Washed The Window FRAME!"
        logging.info("Step 2: Verify that the positive case is passed for the endswith function..")
        assert_that(change_char_in_string(test_text, "endswith", "FRAME!")).is_true()

    def test_case_verify_that_endswith_fun_run_negative(self):
        logging.info("Step 1: Set the test string.")
        test_text = "The Mother Washed The Window FRAME!"
        logging.info("Step 2: Verify that the positive case is passed for the endswith function..")
        assert_that(change_char_in_string(test_text, "endswith", "FRAME")).is_false()

class TestSuitTask05:

    def test_case_verify_that_the_check_on_palindrom_run_positive(self):
        logging.info("Step 1: Set string with palindrom")
        test_text = "ASSA"
        logging.info("Step 2: Verify that all chars are upper in the sentence.")
        assert_that(check_on_palindrom(test_text)).is_true()

    def test_case_verify_that_the_check_on_palindrom_run_negative(self):
        logging.info("Step 1: Set string with NOT palindrom")
        test_text = "ASSAsa"
        logging.info("Step 2: Verify that all chars are upper in the sentence.")
        assert_that(check_on_palindrom(test_text)).is_false()

class TestSuiteTask06:

    def test_case_varify_that_adv_height_calculated_true(self):
        logging.info("Step 1: Set the valid list data with 5 male and 5 femail")
        person_data = {
            'person1': {'gender': 'Male', 'height': 175},
            'person2': {'gender': 'Female', 'height': 160},
            'person3': {'gender': 'Male', 'height': 175},
            'person4': {'gender': 'Male', 'height': 175},
            'person5': {'gender': 'Female', 'height': 165},
            'person6': {'gender': 'Female', 'height': 175},
            'person7': {'gender': 'Male', 'height': 175},
            'person8': {'gender': 'Female', 'height': 167},
            'person9': {'gender': 'Female', 'height': 175},
            'person10': {'gender': 'Male', 'height': 175},
        }
        logging.info("Step 2: Verify that average height value calculated true.")
        assert_that(cal_adv_value_man_height(person_data)).is_equal_to(175.0)

    def test_case_varify_that_caught_typeerror_empty_height_person_data(self):
        logging.info("Step 1: Set the valid list data with 5 male and 5 femail")
        person_data = {
            'person1': {'gender': 'Male', 'height': ""},
            'person2': {'gender': 'Female', 'height': 160},
            'person3': {'gender': 'Male', 'height': 175},
            'person4': {'gender': 'Male', 'height': 175},
            'person5': {'gender': 'Female', 'height': 165},
            'person6': {'gender': 'Female', 'height': 175},
            'person7': {'gender': 'Male', 'height': 175},
            'person8': {'gender': 'Female', 'height': 167},
            'person9': {'gender': 'Female', 'height': 175},
            'person10': {'gender': 'Male', 'height': 175},
        }
        logging.info("Step 2: Verify that average height value calculated true.")
        try:
            cal_adv_value_man_height(person_data)
        except TypeError as e:
            print(f"Caught the error: {e}")

    def test_case_varify_that_caught_typeerror_with_invalid_data_unexpected_person_data(self):
        logging.info("Step 1: Set the valid list data with 5 male and 5 femail")
        person_data = {
            'person1': {'gender': 'Male'},
            'person2': {'gender': 'Female', 'height': 160},
            'person3': {'gender': 'Male', 'height': 175},
            'person4': {'gender': 'Male', 'height': 175},
            'person5': {'gender': 'Female', 'height': 165},
            'person6': {'gender': 'Female', 'height': 175},
            'person7': {'gender': 'Male', 'height': 175},
            'person8': {'gender': 'Female', 'height': 167},
            'person9': {'gender': 'Female', 'height': 175},
            'person10': {'gender': 'Male', 'height': 175},
        }
        logging.info("Step 2: Verify that average height value calculated true.")
        try:
            cal_adv_value_man_height(person_data)
        except KeyError as e:
            print(f"Caught the error: {e}")

    def test_case_varify_that_caught_typeerror_without_male_person_data(self):
        logging.info("Step 1: Set the valid list data with 5 male and 5 femail")
        person_data = {
            'person1': {'gender': 'Female', 'height': 160},
            'person2': {'gender': 'Female', 'height': 160},
            'person3': {'gender': 'Female', 'height': 175},
            'person4': {'gender': 'Female', 'height': 175},
            'person5': {'gender': 'Female', 'height': 165},
            'person6': {'gender': 'Female', 'height': 175},
            'person7': {'gender': 'Female', 'height': 175},
            'person8': {'gender': 'Female', 'height': 167},
            'person9': {'gender': 'Female', 'height': 175},
            'person10': {'gender': 'Female', 'height': 175},
        }
        logging.info("Step 2: Verify that average height value calculated true.")
        try:
            cal_adv_value_man_height(person_data)
        except ZeroDivisionError as e:
            print(f"Caught the error: {e}")