from typing import List, Dict

from src.contexts.shared.domain.domain_event import DomainEvent
from src.contexts.shared.domain.event_bus import EventBus
from src.contexts.shared.domain.event_subscriber import EventSubscriber


class InMemoryEventBus(EventBus):

    def __init__(self, *subscribers: EventSubscriber) -> None:
        event_subscribers_mapping: Dict[str, List[EventSubscriber]] = {}
        for subscriber in subscribers:
            for event in subscriber.subscribed_to():
                if event not in event_subscribers_mapping:
                    event_subscribers_mapping[event] = []
                event_subscribers_mapping[event].append(subscriber)
        self.__subscriptions = event_subscribers_mapping

    def publish(self, events: List[DomainEvent]):
        for event in events:
            event_type = event.get_event_type_name()
            if event_type not in self.__subscriptions:
                continue
            subscribers = self.__subscriptions[event_type]
            for subscriber in subscribers:
                subscriber.on(event)

    def add_subscribers(self, subscribers: List[EventSubscriber]) -> str:
        for subscriber in subscribers:
            self.add_subscriber(subscriber)

    def add_subscriber(self, subscriber: EventSubscriber):
        event_types = subscriber.subscribed_to()
        for event_type in event_types:
            if event_type not in self.__subscriptions:
                self.__subscriptions[event_type] = []
            self.__subscriptions[event_type].append(subscriber)

    def start(self):
        pass
