from uuid import uuid4

from src.contexts.reviews.domain.review import Review
from src.contexts.reviews.domain.review_repository import ReviewRepository
from src.contexts.reviews.domain.value_objects.review_comment import ReviewComment
from src.contexts.reviews.domain.value_objects.review_id import ReviewId
from src.contexts.courses.application.find.course_finder import CourseFinder


class ReviewCreator:
    def __init__(self, repository: ReviewRepository, finder: CourseFinder) -> None:
        self.repository = repository
        self.finder = finder

    def execute(self, course_id: str, comment: ReviewComment):
        self._ensure_course_exists(course_id)
        course = Review.create(ReviewId(str(uuid4())), course_id, ReviewComment(comment))
        self.repository.save(course)
        return course

    def _ensure_course_exists(self, course_id: str):
        self.finder.execute(course_id)
