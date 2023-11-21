""" Course Domain """
from datetime import datetime
from src.contexts.shared.domain.aggregate_root import AggregateRoot
from src.contexts.courses.domain.value_objects.course_id import CourseId


class Course(AggregateRoot):
    id: str
    title: str
    duration: float
    updated_at: datetime
    created_at: datetime

    def __init__(self, id, title, duration, updated_at, created_at) -> None:
        self.id = id
        self.title = title
        self.duration = duration
        self.created_at = created_at
        self.updated_at = updated_at

    @staticmethod
    def create(course_id: CourseId, title: str, duration: float):
        """Creates a new Course."""
        course = Course
        course.id = course_id.value
        course.title = title
        course.duration = duration
        course.updated_at = datetime.now()
        course.created_at = datetime.now()
        return course
