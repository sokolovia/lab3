class ColourFigure:
    def __init__(self, colour):
        self._r, self._g, self._b=colour
    r = property()
    g = property()
    b = property()
    @r.getter
    def r(self):
        return self._r
    @g.getter
    def g(self):
        return self._g
    @b.getter
    def b(self):
        return self._b

    @r.setter
    def r(self, _r):
        self._r=_r
    @g.setter
    def g(self, _g):
        self._g=_g
    @b.setter
    def b(self, _b):
        self._b = _b

