from lesson_l16.task_01.developer import Developer
from lesson_l16.task_01.manager import Manager


class TeamLead(Manager, Developer):
    team_size: int

    def __init__(self, name, salary, department, team_size):
        super().__init__(name, salary, department)
        self.team_size = team_size