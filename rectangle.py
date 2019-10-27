from geometric import *
from colour import *
class Rectangle(GeometricFigure):
    def __init__(self, x, y, colour=(0,0,0)):
        self._x = x
        self._y = y
        self.colour = ColourFigure(colour)
    def calcSquare(self):
        return self._x*self._y
    def __repr__(self):
        return "This is a " + __name__ + " with sides {: f}".format(self._x) + ",{: f}".format(self._y) +  " and colour in rgb format " + "{: d},{: d},{: d}".format(self.colour.r, self.colour.g, self.colour.b)

