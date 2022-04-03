from IChair import IChair


class SmallChair(IChair):

    def __repr__(self):
        return 'Small chair'

    def display(self) -> str:
        return f'Dimension of {repr(self)} are as following{self.dimensions or str(self.default_dimensions)}'

    def __init__(self, **kwargs):
        self.dimensions = kwargs
        self.default_dimensions = {'height': 20, 'width': 20}
