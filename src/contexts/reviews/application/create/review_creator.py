from src.contexts.courses.application.find.course_finder import CourseFinder
from src.contexts.reviews.domain.review import Review
from src.contexts.reviews.domain.review_repository import ReviewRepository


class ReviewCreator:
    def __init__(self, repository: ReviewRepository, finder: CourseFinder) -> None:
        self.repository = repository
        self.finder = finder

    def execute(self, review_id: str, course_id: str, comment: str):
        self._ensure_course_exists(course_id)
        review = Review.create(review_id, course_id, comment)
        self.repository.save(review)
        return review

    def _ensure_course_exists(self, course_id: str):
        self.finder.execute(course_id)
