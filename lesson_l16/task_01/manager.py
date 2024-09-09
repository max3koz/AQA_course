from lesson_l16.task_01.employee import Employee


class Manager(Employee):
    __department: str

    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.__department = department

    def get_department(self):
        return self.__department
