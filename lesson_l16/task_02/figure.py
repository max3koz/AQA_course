from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def calculate_per(self):
        pass

    @abstractmethod
    def calculate_sqr(self):
        pass