from IChair import IChair
from big_chair import BigChair
from medium_chair import MediumChair
from small_chair import SmallChair


class ChairFactory:

    def get_chair(self, chair_type: str) -> IChair:

        if chair_type not in ['b', 's', 'm']:
            raise NotImplementedError(f"Chair type {chair_type} is yet not supported")

        if chair_type == 'b':
            return BigChair(**{'height': 300, 'width': 200})
        elif chair_type == 's':
            return SmallChair(**{'height': 20, 'width': 20})
        elif chair_type == 'm':
            return MediumChair(**{'height': 30, 'width': 30})
