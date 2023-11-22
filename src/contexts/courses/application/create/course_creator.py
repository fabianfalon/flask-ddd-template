from uuid import uuid4

from src.contexts.courses.domain.course import Course
from src.contexts.courses.domain.course_repository import CourseRepository
from src.contexts.courses.domain.errors.course_already_exists import CourseAlreadyExits
from src.contexts.courses.domain.value_objects.course_duration import CourseDuration
from src.contexts.courses.domain.value_objects.course_id import CourseId
from src.contexts.courses.domain.value_objects.course_title import CourseTitle


class CourseCreator:
    def __init__(self, repository: CourseRepository) -> None:
        self.repository = repository

    def execute(self, title: str, duration: float):
        title = CourseTitle(title)
        recorded = self.repository.find_one_by_title(title.value.lower().strip())
        if recorded:
            raise CourseAlreadyExits()

        course = Course.create(CourseId(str(uuid4())), title, CourseDuration(duration))
        self.repository.save(course)
        return course
