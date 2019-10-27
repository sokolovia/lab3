from geometric import *
from colour import *
from math import pi
class Circle(GeometricFigure):
    def __init__(self, r, colour=(0,0,0)):
        self._r = r
        self.colour = ColourFigure(colour)
    def calcSquare(self):
        return self._r * self._r * pi
    def __repr__(self):
        return "This is a " + __name__ + " with radius {: f}".format(self._r) + " and colour in rgb format " + "{: d},{: d},{: d}".format(self.colour.r, self.colour.g, self.colour.b)
       