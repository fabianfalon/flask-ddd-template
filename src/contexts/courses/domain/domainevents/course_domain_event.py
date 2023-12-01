from datetime import datetime
from typing import Optional

from src.contexts.shared.domain.aggregate_root import AggregateRoot
from src.contexts.shared.domain.domain_event import DomainEvent


class CourseCreatedEvent(DomainEvent):
    EVENT_TYPE = "contexts.courses.domain.course.created"

    def __init__(
        self,
        aggregate_id: str,
        entity: AggregateRoot,
        event_id: Optional[str] = None,
        occurred_on: Optional[datetime] = None,
    ):
        super().__init__(self.EVENT_TYPE, aggregate_id, event_id, occurred_on)
        self.entity = entity

    def to_primitives(self):
        return {
            "data": {
                "id": self.event_id,
                "aggregate_id": self.aggregate_id,
                "occurred_on": self.occurred_on,
                "created_at": self.created_at,
                "type": CourseCreatedEvent.EVENT_TYPE,
                "attributes": self.entity.to_primitive()
            },
            "metadata": {}
        }

    def from_primitives(self, aggregate_id: str, event_id: str, occurred_on: datetime, attributes: dict):
        pass

