from lesson_l16.task_01.employee import Employee


class Developer(Employee):

    __programming_language: str

    def get_programming_language(self):
        return self.__programming_language
