class Rhombus:

    __side: float
    __angle_a: float
    __angle_b: float

    def __init__(self, side: float, angle: float):
        self.__set_side_value(side)
        self.__set_angle_values(angle)

    def __set_side_value(self, side_new: float) -> None:
        """
        Set side_a and side_b values with verify condition:
        1/ The value of the side side_a must be greater than 0.
        """
        if side_new > 0: # condition 1
            setattr(self, "_Rhombus__side", side_new) # condition 4
        else:
            raise ValueError(f"The length of rhombus side must be positive number! "
                             f"You entered negative number: {side_new}.")


    def __set_angle_values(self, angle_new: float)-> None:
        """
        Set angle_a and angle_b values with verify conditions:
        1/ Angles angle_a and angle_b must be filled with the condition: angle_a + angle_a = 180.
        2/ Opposite angles of a rhombus are always equal, therefore, given the value of angle_a,
           the value of angle_b is automatically calculated.
        """
        if 0 < angle_new < 180: # condition 1
            setattr(self, "_Rhombus__angle_a", angle_new) # condition 4
            setattr(self, "_Rhombus__angle_b", 180 - angle_new) # condition 2, 3
        else:
            raise ValueError(f"The length of rhombus angle_a must be from 1 till 179! "
                             f"You entered negative number: {angle_new}.")

    def get_side_value(self):
        return self.__side

    def get_angle_a(self):
        return self.__angle_a

    def get_angle_b(self):
        return self.__angle_b
