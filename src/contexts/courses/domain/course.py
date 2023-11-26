""" Course Domain """
from datetime import datetime

from src.contexts.courses.domain.value_objects.course_duration import CourseDuration
from src.contexts.courses.domain.value_objects.course_title import CourseTitle
from src.contexts.shared.domain.aggregate_root import AggregateRoot
from src.contexts.shared.domain.value_objects.course_id import CourseId


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
        created_at: None,
        updated_at: None,
    ) -> None:
        self.id = course_id
        self.title = title
        self.duration = duration
        self.created_at = datetime.now() if not created_at else created_at
        self.updated_at = datetime.now() if not updated_at else updated_at
