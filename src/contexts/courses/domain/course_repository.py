from typing import List, NoReturn, Optional

from abc import ABC, abstractmethod

from src.contexts.courses.domain.course import Course
from src.contexts.shared.domain.criteria.criteria import Criteria


class CourseRepository(ABC):
    """docstring for CourseRepository"""

    @abstractmethod
    def save(self, course: Course) -> Course:
        ...

    @abstractmethod
    def delete(self, course_id: str) -> NoReturn:
        ...

    @abstractmethod
    def find_one(self, course_id: str) -> Optional[Course]:
        ...

    @abstractmethod
    def find_all(self) -> List[Course]:
        ...

    @abstractmethod
    def matching(self, criteria: Criteria) -> List[Course]:
        ...

    @abstractmethod
    def find_one_by_title(self, title) -> Course:
        ...
