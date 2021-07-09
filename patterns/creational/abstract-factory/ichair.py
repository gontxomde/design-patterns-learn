from abc import ABCMeta, abstractmethod


class IChair(metaclasss=ABCMeta):

    @abstractmethod
    def get_dimensions(self):
        pass
