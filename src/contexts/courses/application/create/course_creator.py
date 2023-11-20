from uuid import uuid4

from src.contexts.courses.domain.course import Course
from src.contexts.courses.domain.course_repository import CourseRepository
from src.contexts.courses.domain.errors.course_already_exists import CourseAlreadyExits
from src.contexts.courses.domain.value_objects.course_id import CourseId


class CourseCreator:
    def __init__(self, repository: CourseRepository) -> None:
        self.repository = repository

    def execute(self, title: str, duration: float):
        recorded = self.repository.find_one_by_title(title.lower().strip())
        if recorded:
            raise CourseAlreadyExits()

        course_id = CourseId(str(uuid4()))
        course = Course.create(course_id, title, duration)
        self.repository.save(course)
        return course
