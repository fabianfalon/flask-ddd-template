""" Course Domain """
from datetime import datetime

from src.contexts.courses.domain.value_objects.course_duration import CourseDuration
from src.contexts.courses.domain.value_objects.course_title import CourseTitle
from src.contexts.shared.domain.aggregate_root import AggregateRoot
from src.contexts.shared.domain.value_objects.course_id import CourseId


class Course(AggregateRoot):
    _id: CourseId
    _title: CourseTitle
    _duration: CourseDuration
    updated_at: datetime
    created_at: datetime

    def __init__(
        self,
        course_id: str,
        title: str,
        duration: float,
        created_at: None,
        updated_at: None,
    ) -> None:
        self._id = CourseId(course_id)
        self._title = CourseTitle(title)
        self._duration = CourseDuration(duration)
        self.created_at = datetime.now() if not created_at else created_at
        self.updated_at = datetime.now() if not updated_at else updated_at

    @property
    def id(self):
        return self._id.value

    @property
    def title(self):
        return self._title.value

    @property
    def duration(self):
        return self._duration.value

    @staticmethod
    def from_primitive(_id, title, duration, created_at, updated_at):
        return Course(
            course_id=_id,
            title=title,
            duration=duration,
            created_at=created_at,
            updated_at=updated_at,
        )

    @staticmethod
    def create(course_id, title, duration):
        """Creates a new Course."""
        course = Course(
            course_id=course_id,
            title=title,
            duration=duration,
            updated_at=datetime.now(),
            created_at=datetime.now(),
        )

        # logic to public domain event
        return course
