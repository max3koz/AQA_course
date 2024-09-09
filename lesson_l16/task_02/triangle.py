from math import sqrt

from lesson_l16.task_02.figure import Figure

class Triangle(Figure):
    __side_a: int
    __side_b: int
    __side_c: int

    def __init__(self, side_a, side_b, side_c):
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c

    def calculate_per(self):
        return self.__side_a + self.__side_b + self.__side_c

    def calculate_sqr(self) -> float:
        p = (self.__side_a + self.__side_b + self.__side_c) / 2
        return sqrt(p * (p - self.__side_a) * (p - self.__side_b) * (p - self.__side_c))