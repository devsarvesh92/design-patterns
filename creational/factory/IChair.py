from abc import ABCMeta
from abc import abstractmethod


class IChair(metaclass=ABCMeta):

    @abstractmethod
    def display(self) -> str:
        raise NotImplementedError
