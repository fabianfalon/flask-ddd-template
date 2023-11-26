""" Review Domain """
from datetime import datetime

from src.contexts.reviews.domain.value_objects.review_comment import ReviewComment
from src.contexts.reviews.domain.value_objects.review_id import ReviewId
from src.contexts.shared.domain.aggregate_root import AggregateRoot
from src.contexts.shared.domain.value_objects.course_id import CourseId


class Review(AggregateRoot):
    review_id: str
    course_id: str
    comment: str
    updated_at: datetime
    created_at: datetime

    def __init__(
        self,
        review_id: ReviewId,
        course_id: CourseId,
        comment: ReviewComment,
        updated_at,
        created_at,
    ) -> None:
        self.review_id = review_id
        self.course_id = course_id
        self.comment = comment
        self.created_at = created_at
        self.updated_at = updated_at

    @staticmethod
    def create(review_id: ReviewId, course_id: CourseId, comment: ReviewComment):
        """Creates a new Review."""
        return Review(
            review_id=review_id.value,
            course_id=course_id.value,
            comment=comment.value,
            updated_at=datetime.now(),
            created_at=datetime.now(),
        )
