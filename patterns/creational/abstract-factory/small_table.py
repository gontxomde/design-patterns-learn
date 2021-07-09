from itable import ITable


class SmallTable(ITable):

    def __init__(self):
        self._height = 41
        self._width = 40
        self._depth = 40

    def get_dimensions(self):
        return {
            'width': self._width,
            'depth': self._depth,
            'height': self._height
        }
