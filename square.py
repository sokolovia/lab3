from rectangle import *
class Square(Rectangle):
    def __init__(self, x, colour=(...)):
        return super().__init__(x, x, colour=colour)
    def __repr__(self):
        return super().__repr__()