from abc import ABC, abstractmethod
from datetime import datetime
from uuid import uuid4


class DomainEvent(ABC):

    def __init__(self, event_name: str, aggregate_id: str, event_id: str, occurred_on: datetime) -> None:
        self.event_name = event_name
        self.aggregate_id = aggregate_id
        self.event_id = event_id if event_id else str(uuid4())
        self.occurred_on = occurred_on if occurred_on else datetime.utcnow()
        self.created_at = datetime.utcnow()

    @abstractmethod
    def to_primitives(self):
        ...

    def get_event_type_name(self) -> str:
        return self.event_name

    @abstractmethod
    def from_primitives(
        self, aggregate_id: str, event_id: str, occurred_on: datetime, attributes: dict
    ):
        return DomainEvent(
            aggregate_id=aggregate_id,
            event_id=event_id,
            occurred_on=occurred_on,
            attributes=attributes,
        )
