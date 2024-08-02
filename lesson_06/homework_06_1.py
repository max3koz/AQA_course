"""Task_01"""

input_string: str = input("Enter string: ")

unique_chars_counter: int = sum([1 for char in input_string if input_string.count(char) == 1])

if unique_chars_counter > 10:
    print(True)
else:
    print(False)

"""#=============================================="""
"""Task_02"""

is_correct_string = False
while not is_correct_string:
    input_string: str = input("Enter string: ").lower()
    if input_string.find("h") != -1:
        is_correct_string = True

"""#=============================================="""
"""Task_03"""

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

lst2 = [item for item in lst1 if isinstance(item, str)]
print(lst2)

"""#=============================================="""
"""Task_04"""

enter_list: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num_sum: int = sum([num for num in enter_list if num % 2 == 0])
print(num_sum)
