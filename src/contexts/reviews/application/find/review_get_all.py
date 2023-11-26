from src.contexts.reviews.domain.review import Review
from src.contexts.reviews.domain.review_repository import ReviewRepository
from src.contexts.shared.domain.value_objects.course_id import CourseId

from typing import List


class ReviewGetAllByCourse:
    def __init__(self, repository: ReviewRepository) -> None:
        self.repository = repository

    def execute(self, course_id: CourseId) -> List[Review]:
        reviews = self.repository.find_by_course_id(course_id)
        return reviews
