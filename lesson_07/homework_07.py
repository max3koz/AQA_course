print("\nTask01.\nЗадача - надрукувати табличку множення на задане число, але лише до максимального значення "
      "для добутку - 25. Код майже готовий, треба знайти помилки та випраавити/доповнити.")


def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1
    max_value = 25
    result = 0

    # Complete the while loop condition.
    while result < max_value:
        result = number * multiplier
        # десь тут помила, а може не одна
        if result > max_value:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1


multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


print("\nTask02.\nНаписати функцію, яка обчислює суму двох чисел.")


def sum_of_2_nums(num_1: int, num_2: int) -> int:
    return num_1 + num_2


print(sum_of_2_nums(2, 3))


print("\nTask03.\nНаписати функцію, яка розрахує середнє арифметичне списку чисел.")


def middle_of_nums(nums_list: list) -> float:
    return sum(nums_list)/len(nums_list)


print(middle_of_nums([1, 2, 3, 4, 5]))


print("\nTask04.\nНаписати функцію, яка приймає рядок та повертає його у зворотному порядку.")


def revers_list(new_string: str) -> str:
    return new_string[::-1]


print(revers_list("Please revers this string!!!"))


print("\nTask05.\nНаписати функцію, яка приймає список слів та повертає найдовше слово у списку.")


def longer_word(words_list: list) -> str:
    longest_word = ""
    longest_word_length = 0
    for string_item in words_list:
        if longest_word_length < len(string_item):
            longest_word_length = len(string_item)
            longest_word = string_item
    return longest_word


print(longer_word(["qwe", "asdf", "rt", "oiuyt", "xcvb"]))


print("\nTask6.\nНаписати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка"
      "у перший рядок, якщо другий рядок є підрядком першого рядка, "
      "та -1, якщо другий рядок не є підрядком першого рядка.")


def find_substring(str1, str2):
    return str1.find(str2)


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

"""
Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

print("\nTask07.\nЗробіть так, щоб у тексті було не більше одного пробілу між словами.")

adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""


def delete_extera_gap(string: str) -> str:
    return " ".join(string.split())


print(delete_extera_gap(adwentures_of_tom_sawer))


print("\nTask08.\nВиведіть, скільки слів у тексті починається з Великої літери?")


def sum_of_title_word(string: str) -> int:
    count = 0
    for word in string.split():
        if word.istitle():
            count += 1
    return count


print(f"There are {sum_of_title_word(delete_extera_gap(adwentures_of_tom_sawer))} times the word with title in the sentence "
      f"\"adwentures_of_tom_sawer\".")


print("\nTask09.\nВиведіть, скількі разів у тексті зустрічається літера \"h\"")

def calculate_letter_in_string(find_char: str) -> int:
    count = 0
    for letter in adwentures_of_tom_sawer:
        if letter == "h":
            count += 1
    return count

print(f"There are {calculate_letter_in_string('h')} times the letter \"h\" "
      f"in the sentence \"adwentures_of_tom_sawer\".")



print("\nTask10.\n"
      "Знайди остачу від діленя чисел:"
      "a) 8019 : 8, d) 7248 : 6, b) 9907 : 9, e) 7128 : 5, c) 2789 : 5, f) 19224 : 9")

def get_division_remainder(num_1: int, num_2: int) -> float:
    return num_1 % num_2

num_dict = {8019: 8, 7248: 6, 9907: 9, 7128: 5, 2789: 5, 19224: 9}

print("Залишок від ділення:")
for divisible, divisor in num_dict.items():
    print(f"    {divisible} на {divisor} - {get_division_remainder(divisible, divisor)}")
