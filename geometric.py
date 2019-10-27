import abc
class GeometricFigure(abc.ABC):
    @abc.abstractmethod
    def calcSquare(self):
        return self.x * self.y
