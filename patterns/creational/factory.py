from abc import ABCMeta, abstractmethod


class IChair(metaclass=ABCMeta):

    @abstractmethod
    def get_dimensions(self):
        pass


class SmallChair(IChair):

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


class MediumChair(IChair):

    def __init__(self):
        self._height = 61
        self._width = 60
        self._depth = 60

    def get_dimensions(self):
        return {
            'width': self._width,
            'depth': self._depth,
            'height': self._height
        }


class BigChair(IChair):

    def __init__(self):
        self._height = 71
        self._width = 70
        self._depth = 70

    def get_dimensions(self):
        return {
            'width': self._width,
            'depth': self._depth,
            'height': self._height
        }


class ChairFactory:

    @staticmethod
    def get_chair(chair_type: str) -> IChair:
        if chair_type == 'BigChair':
            return BigChair()
        elif chair_type == 'MediumChair':
            return MediumChair()
        elif chair_type == 'SmallChair':
            return SmallChair()
        else:
            return None


chair = ChairFactory().get_chair('SmallChair')
