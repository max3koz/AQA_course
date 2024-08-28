person_data = {
    'person1': {'gender': 'Male', 'height': 175},
    'person2': {'gender': 'Female', 'height': 160},
    'person3': {'gender': 'Male', 'height': 180},
    'person4': {'gender': 'Male', 'height': 175},
    'person5': {'gender': 'Female', 'height': 165},
    'person6': {'gender': 'Male', 'height': 185},
    'person7': {'gender': 'Male', 'height': 177},
    'person8': {'gender': 'Female', 'height': 167},
    'person9': {'gender': 'Male', 'height': 187},
    'person10': {'gender': 'Male', 'height': 188},
}


def cal_middle_man_height(persons: dict[str, dict[str, int]]) -> float:
    new_dict = [person["height"] for person in persons.values() if person['gender'] == 'Male']
    return sum(new_dict)/len(new_dict)

print(cal_middle_man_height(person_data))