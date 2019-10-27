from circle import *
from rectangle import *
from square import *

blue_rectangle = Rectangle(3, 2, (0,83,138))
for figures in [Rectangle(3, 2, (0,0,255)), Circle(5, (0,255,0)), Square(5, (255,0,0))]: print(figures)