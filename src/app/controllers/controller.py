from abc import ABC, abstractmethod

from src.contexts.courses.domain.course import Course


class ControllerInterfaz(ABC):
    """ControllerInterfaz"""

    @abstractmethod
    def execute(self, course: Course) -> Course:
        ...
