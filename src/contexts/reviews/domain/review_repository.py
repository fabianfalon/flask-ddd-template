from typing import List, NoReturn, Optional

from abc import ABC, abstractmethod

from src.contexts.reviews.domain.review import Review
from src.contexts.shared.domain.criteria.criteria import Criteria
from src.contexts.shared.domain.value_objects.course_id import CourseId


class ReviewRepository(ABC):
    """docstring for ReviewRepository"""

    @abstractmethod
    def save(self, course: Review) -> Review:
        ...

    @abstractmethod
    def delete(self, review_id: str) -> NoReturn:
        ...

    @abstractmethod
    def find_one(self, review_id: str) -> Optional[Review]:
        ...

    @abstractmethod
    def find_all(self) -> List[Review]:
        ...

    @abstractmethod
    def matching(self, criteria: Criteria) -> List[Review]:
        ...

    @abstractmethod
    def find_by_course_id(self, course_id: CourseId) -> Review:
        ...
