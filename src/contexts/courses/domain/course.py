""" Course Domain """
from datetime import datetime

from src.contexts.courses.domain.value_objects.course_id import CourseId


class Course:
    id: str
    title: str
    duration: float
    updated_at: datetime
    crated_at: datetime

    @classmethod
    def create(cls, course_id: CourseId, title: str, duration: float):
        """Creates a new Course."""
        course = Course()
        course.id = course_id.value
        course.title = title
        course.duration = duration
        course.updated_at = datetime.now()
        course.crated_at = datetime.now()
        return course
