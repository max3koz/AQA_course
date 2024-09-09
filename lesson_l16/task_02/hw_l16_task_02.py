from lesson_l16.task_02.figure import Figure
from lesson_l16.task_02.rectangle import Rectangle
from lesson_l16.task_02.square import Square
from lesson_l16.task_02.triangle import Triangle

square_first: Square = Square(5)
rectangle_first: Rectangle = Rectangle(5, 10)
triangle_first: Triangle = Triangle(5, 6, 7)

figures_list: list[Figure] = [square_first, rectangle_first, triangle_first]

figures_param_list: list[list] = [[figure.calculate_per(), figure.calculate_sqr()] for figure in figures_list]

for item in figures_param_list:
    print(f"The perimeter of figure is {item[0]} and the square is {item[1]}")
