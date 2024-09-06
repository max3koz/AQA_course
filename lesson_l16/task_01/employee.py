from abc import ABC


class Employee(ABC):
    name: str
    salary: int

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
