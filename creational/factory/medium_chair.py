from IChair import IChair


class MediumChair(IChair):

    def __repr__(self):
        return 'Medium chair'

    def display(self) -> str:
        return f'Dimension of {repr(self)} are as following{self.dimensions or str(self.default_dimensions)}'

    def __init__(self, **kwargs):
        self.dimensions = kwargs
        self.default_dimensions = {'height': 30, 'width': 30}
