from lesson_l16.task_02.figure import Figure

class Rectangle(Figure):
    __side_a: int
    __side_b: int

    def __init__(self, side_a, side_b):
        self.__side_a = side_a
        self.__side_b = side_b


    def calculate_per(self):
        return 2 * (self.__side_a + self.__side_b)

    def calculate_sqr(self):
        return self.__side_a * self.__side_b