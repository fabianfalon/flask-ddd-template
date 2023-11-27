""" Review Domain """
from datetime import datetime

from src.contexts.reviews.domain.value_objects.review_comment import ReviewComment
from src.contexts.reviews.domain.value_objects.review_id import ReviewId
from src.contexts.shared.domain.aggregate_root import AggregateRoot
from src.contexts.shared.domain.value_objects.course_id import CourseId


class Review(AggregateRoot):
    _review_id: ReviewId
    _course_id: CourseId
    _comment: ReviewComment
    updated_at: datetime
    created_at: datetime

    def __init__(
        self,
        review_id: str,
        course_id: str,
        comment: str,
        updated_at: None,
        created_at: None,
    ) -> None:
        self._review_id = ReviewId(review_id)
        self._course_id = CourseId(course_id)
        self._comment = ReviewComment(comment)
        self.created_at = datetime.now() if not created_at else created_at
        self.updated_at = datetime.now() if not updated_at else updated_at

    @property
    def review_id(self):
        return self._review_id.value

    @property
    def course_id(self):
        return self._course_id.value

    @property
    def comment(self):
        return self._comment.value

    @staticmethod
    def create(review_id, course_id, comment):
        """Creates a new Review."""
        review = Review(
            review_id=review_id,
            course_id=course_id,
            comment=comment,
            updated_at=datetime.now(),
            created_at=datetime.now(),
        )

        # logic to public domain event
        return review
