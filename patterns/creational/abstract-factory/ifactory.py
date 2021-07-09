from abc import ABCMeta, abstractmethod


class IFactory(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def get_furniture(obj_type):
        pass
