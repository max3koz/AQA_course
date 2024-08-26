from pymacaroons.utils import equals


def word_count(text_string: str) ->int:
    return len(text_string.split())

def concatenate_strings(string_list: list[str], symbol: str) -> str:
    return symbol.join(string_list)

def change_char_in_string(text_string: str, action: str, prefix: str):
    if action is "upper":
       return text_string.upper()
    elif action is "lower":
        return text_string.lower()
    elif action is "startswith":
        return text_string.startswith(prefix)
    elif action is "endswith":
        return text_string.endswith(prefix)
    else:
        return "This option is not support!"

def check_on_palindrom(word: str) -> bool:
    return word == word[::-1]

def cal_adv_value_man_height(persons: dict[str, dict[str, int]]) -> float:
    new_dict = [person["height"] for person in persons.values() if person['gender'] == 'Male']
    return sum(new_dict)/len(new_dict)


