from lesson_l16.task_01.employee import Employee


class Manager(Employee):
    department: str

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
