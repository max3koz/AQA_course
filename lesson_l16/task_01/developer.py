from lesson_l16.task_01.employee import Employee


class Developer(Employee):

    __programming_language: str

    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.__programming_language = programming_language

    def get_programming_language(self):
        return self.__programming_language
