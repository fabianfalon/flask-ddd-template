""" Course Domain """
from datetime import datetime

from src.contexts.courses.domain.value_objects.course_duration import CourseDuration
from src.contexts.shared.domain.value_objects.course_id import CourseId
from src.contexts.courses.domain.value_objects.course_title import CourseTitle
from src.contexts.shared.domain.aggregate_root import AggregateRoot


class Course(AggregateRoot):
    id: str
    title: str
    duration: float
    updated_at: datetime
    created_at: datetime

    def __init__(
            self,
            course_id: CourseId,
            title: CourseTitle,
            duration: CourseDuration,
            updated_at,
            created_at,
    ) -> None:
        self.id = course_id
        self.title = title
        self.duration = duration
        self.created_at = created_at
        self.updated_at = updated_at

    @staticmethod
    def create(course_id: CourseId, course_title: CourseTitle, duration: CourseDuration):
        """Creates a new Course."""
        return Course(
            course_id=course_id.value,
            title=course_title.value,
            duration=duration.value,
            updated_at=datetime.now(),
            created_at=datetime.now(),
        )
