from abc import ABC, abstractmethod
from typing import List

from src.contexts.shared.domain.domain_event import DomainEvent


class EventBus(ABC):

    @abstractmethod
    def publish(self, events: List[DomainEvent]):
        ...

    @abstractmethod
    def add_subscribers(self) -> str:
        ...

    @abstractmethod
    def start(self):
        ...
