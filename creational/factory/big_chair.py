from IChair import IChair


class BigChair(IChair):

    def __repr__(self):
        return 'BigChair'

    def display(self) -> str:
        return f'Dimension of {repr(self)} chair are as following{self.dimensions or str(self.default_dimensions)}'

    def __init__(self, **kwargs):
        self.dimensions = kwargs
        self.default_dimensions = {'height': 100, 'width': 100}
