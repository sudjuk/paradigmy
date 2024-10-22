from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.color} {self.area():.2f} sq. units"
