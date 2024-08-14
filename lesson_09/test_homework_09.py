import unittest
from homework_09 import (longer_word, get_division_remainder, find_substring,
                         middle_of_nums, revers_list)


class TestSuiteLongerWord(unittest.TestCase):
    def test_verify_that_find_longer_word(self):
        # Create possitive test sample
        test_valid_list = ["qwe", "asdf", "rt", "oiuyt", "xcvb"]
        # Get result
        result = longer_word(test_valid_list)
        # Get positive result
        self.assertEqual(result, "oiuyt")

    def test_negative_find_longer_word(self):
        # Create negative test sample
        test_valid_list = ["qwe", "asdf", 5, "oiuyt", "xcvb"]
        # Get exeption
        with self.assertRaises(TypeError):
            longer_word(test_valid_list)


class TestSuiteDivRemainder(unittest.TestCase):
    def test_positive_DivRemainder_case(self):
        # Create possitive test sample
        test_valid_num_1 = 2
        test_valid_num_2 = 3
        # Get result
        result = get_division_remainder(test_valid_num_1, test_valid_num_2)
        # Get positive result
        self.assertEqual(result, 2)

    def test_negative_DivRemainder_case(self):
        # Create negative test sample
        test_num_1 = 2
        test_zero_num = 0
        # Get exeption
        with self.assertRaises(ZeroDivisionError):
            get_division_remainder(test_num_1, test_zero_num)


class TestSuiteFindSubstring(unittest.TestCase):
    def test_positive_case_find_substring(self):
        # Create possitive test sample
        test_string_1 = "Hello, world!"
        test_string_2 = "world"
        # Get result
        result = find_substring(test_string_1, test_string_2)
        # Get positive result
        self.assertEqual(result, 7)

    def test_negative_case_find_substring(self):
        # Create negative test sample with integer
        test_string_1 = "Hello, world!"
        test_vstring_2 = 5
        # Get exeption
        with self.assertRaises(TypeError):
            find_substring(test_string_1, test_vstring_2)


class TestSuiteTaskMiddleOfNums(unittest.TestCase):
    def test_positive_numbers(self):
        # Create possitive test sample
        test_valid_list = [1, 2, 3, 4, 5]
        # Get result
        result = middle_of_nums(test_valid_list)
        # Get positive result
        self.assertEqual(result, 3)

    def test_add_negative_numbers(self):
        # Create negative test sample
        test_valid_list = [1, 2, 3, 4, "p"]
        # Get exeption
        with self.assertRaises(TypeError):
            middle_of_nums(test_valid_list)
       

class TestSuiteReversList(unittest.TestCase):
    def test_positive_revers_list(self):
        # Create positive test sample
        test_string = "!!!gnirts siht srever esaelP"
        # Get result
        result = revers_list(test_string)
        # Get positive result
        self.assertEqual(result, "Please revers this string!!!")

    def test_negative_revers_list_invalid_data_type(self):
        # Create negative test sample unexpected sentence
        test_string = {"!!!gnirts siht srever esaelP"}
        # Get exeption
        with self.assertRaises(TypeError):
            revers_list(test_string)


if __name__ == '__main__':
    unittest.main()
