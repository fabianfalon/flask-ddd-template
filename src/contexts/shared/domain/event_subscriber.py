from abc import ABC, abstractmethod
from typing import List

from src.contexts.shared.domain.domain_event import DomainEvent


class EventSubscriber(ABC):

    @abstractmethod
    def subscribed_to(self) -> List[str]:
        ...

    @abstractmethod
    def on(self, domain_event: DomainEvent):
        ...
