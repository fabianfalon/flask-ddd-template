from typing import List

from src.contexts.reviews.domain.review import Review
from src.contexts.reviews.domain.review_repository import ReviewRepository


class ReviewGetAllByCourse:
    def __init__(self, repository: ReviewRepository) -> None:
        self.repository = repository

    def execute(self, course_id) -> List[Review]:
        reviews = self.repository.find_by_course_id(course_id)
        return reviews
