from abc import ABC, abstractmethod
from typing import List

from src.contexts.shared.domain.domain_event import DomainEvent


class AggregateRoot(ABC):

    def __init__(self):
        self._domain_events: List[DomainEvent] = []

    @abstractmethod
    def to_primitive(self):
        ...

    @abstractmethod
    def from_primitive(self, raw_data: dict):
        ...

    def pull_domain_events(self):
        events = self._domain_events
        self._domain_events = []
        return events

    def record_events(self, event: DomainEvent):
        self._domain_events.append(event)
