class Student:

    name: str
    surname: str
    age: int
    avd_mark: float

    def __init__(self, name, surname, age, avd_mark):
        self.name = name
        self.surname = surname
        self.age = age
        self.avd_mark = avd_mark

    def change_avd_mark(self, new_avd_mark):
        self.avd_mark = new_avd_mark
        print(f"The avd_mark was changed to {self.avd_mark}")
