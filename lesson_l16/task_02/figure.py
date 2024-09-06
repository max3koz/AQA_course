from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def calculate_per(self):
        pass

    @abstractmethod
    def calculate_sqr(self):
        pass

class Square(Figure):

    __square_side: int

    def __init__(self, square_side):
        self.square_side = square_side

    def calculate_per(self):
        pass

    def calculate_sqr(self):
        pass


class Rectangle(Figure):
    __side_a: int
    __side_b: int

    def __init__(self, side_a, side_b):
        self.__side_a = side_a
        self.__side_a = side_b


    def calculate_per(self):
        pass

    def calculate_sqr(self):
        pass