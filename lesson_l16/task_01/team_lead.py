from lesson_l16.task_01.developer import Developer
from lesson_l16.task_01.manager import Manager


class TeamLead(Manager, Developer):
    __team_size: int

    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.__team_size = team_size

    def get_team_size(self):
        return self.__team_size
