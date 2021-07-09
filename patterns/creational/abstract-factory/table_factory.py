from ifactory import IFactory
from small_table import SmallTable
from medium_table import MediumTable


class TableFactory:

    @staticmethod
    def get_table(obj_type):
        if obj_type == 'MediumTable':
            return MediumTable()

        elif obj_type == 'SmallTable':
            return SmallTable()

        else:
            return None
