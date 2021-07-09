from ifactory import IFactory
from small_chair import SmallChair
from medium_chair import MediumChair


class ChairFactory():

    @staticmethod
    def get_chair(obj_type):
        if obj_type == 'MediumChair':
            return MediumChair()
        elif obj_type == 'SmallChair':
            return SmallChair()
        else:
            return None
