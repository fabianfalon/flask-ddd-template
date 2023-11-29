from abc import ABC, abstractmethod


class AggregateRoot(ABC):

    @abstractmethod
    def to_primitive(self):
        ...

    @abstractmethod
    def from_primitive(self, raw_data: dict):
        ...
