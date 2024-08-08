"""
Створіть масив зі строками, які будуть складатися з чисел, які розділені комою.
Наприклад: [”1,2,3,4”, ”1,2,3,4,50” ”qwerty1,2,3”]
Для кожного елементу списку виведіть суму всіх чисел (створіть нову функцію для цього).
Якщо є символи, що не є числами (”qwerty1,2,3” у прикладі), вам потрібно зловити вийняток
і вивести “Не можу це зробити!”
Використовуйте блок try\except, щоб уникнути інших символів, окрім чисел у списку.
Для цього прикладу правильний вивід буде - 10, 60, “Не можу це зробити”
"""

test_list_with_string = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]
test_list_with_string_1 = ["1,2,3,4", "1,2,3,4,50", "1,2,3"]


def sum_all_item_from_string(test_list: list[str]) -> None:
    for item in test_list:
        chars_list = item.split(",")
        try:
            result = (sum(int(integer) for integer in chars_list))
            print(result)
        except (ValueError, TypeError) as exception:
            print(f"Не можу це зробити! Exception: {exception}")


# Check with wrong data
sum_all_item_from_string(test_list_with_string)
# Check with correct data
sum_all_item_from_string(test_list_with_string_1)
