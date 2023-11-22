from uuid import uuid4

from src.contexts.reviews.domain.review import Review
from src.contexts.reviews.domain.review_repository import ReviewRepository
from src.contexts.reviews.domain.value_objects.review_comment import ReviewComment
from src.contexts.reviews.domain.value_objects.review_id import ReviewId


class ReviewCreator:
    def __init__(self, repository: ReviewRepository) -> None:
        self.repository = repository

    def execute(self, course_id: str, comment: ReviewComment):
        course = Review.create(ReviewId(str(uuid4())), course_id, ReviewComment(comment))
        self.repository.save(course)
        return course
