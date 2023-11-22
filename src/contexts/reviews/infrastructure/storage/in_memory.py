from typing import List, NoReturn, Optional

from src.contexts.reviews.domain.review import Review
from src.contexts.reviews.domain.review_repository import ReviewRepository


class InMemoryReviewRepository(ReviewRepository):
    _reviews: List[Review] = []

    def save(self, review: Review) -> Review:
        self._reviews.append(review)

    def delete(self, course_id: str) -> NoReturn:
        pass

    def find_one(self, course_id: str) -> Optional[Review]:
        return next(filter(lambda x: (x.id == course_id), self._reviews), None)

    def find_all(self) -> List[Review]:
        return self._reviews

    def matching(self, criteria):
        pass

    def find_one_by_course_id(self, course_id) -> Optional[Review]:
        return next(filter(lambda x: (x.course_id == course_id), self._reviews), None)

    def clear(self):
        self._reviews = []
