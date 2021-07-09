from ifactory import IFactory
from chair_factory import ChairFactory
from table_factory import TableFactory

class FurnitureFactory(IFactory):

    @staticmethod
    def get_furniture(obj_type):
        if "table" in obj_type:
            return TableFactory.get_table(obj_type)
        if 'chair' in obj_type:
            return ChairFactory.get_chair(obj_type)