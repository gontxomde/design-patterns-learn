from abc import ABCMeta, abstractmethod


class ITable(metaclasss=ABCMeta):

    @abstractmethod
    def get_dimensions(self):
        pass
