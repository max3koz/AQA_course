def longer_word(words_list: list) -> str:
    """
    Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
    """
    longest_word = ""
    longest_word_length = 0
    for string_item in words_list:
        if longest_word_length < len(string_item):
            longest_word_length = len(string_item)
            longest_word = string_item
    return longest_word


def get_division_remainder(num_1: int, num_2: int) -> float:
    """
    Знайди остачу від діленя чисел.
    """
    return num_1 % num_2


def find_substring(str1, str2):
    """
    Написати функцію, яка приймає два рядки та повертає індекс першого входження другого
    рядка у перший рядок, якщо другий рядок є підрядком першого рядка, та -1,
    якщо другий рядок не є підрядком першого рядка.")
    """
    return str1.find(str2)


def middle_of_nums(nums_list: list):
    """
    Написати функцію, яка розрахує середнє арифметичне списку чисел.")
    """
    if len(nums_list) != 0:
        return sum(nums_list)/len(nums_list)
    else:
        return None


def revers_list(new_string: str) -> str:
    """
    Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
    """
    return "".join(reversed(new_string))
