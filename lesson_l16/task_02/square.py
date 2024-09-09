from lesson_l16.task_02.figure import Figure


class Square(Figure):

    __square_side: int

    def __init__(self, square_side):
        self.square_side = square_side

    def calculate_per(self):
        return self.square_side * 4

    def calculate_sqr(self):
        return self.square_side * self.square_side