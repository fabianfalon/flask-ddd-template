from src.contexts.courses.domain.course import Course
from src.contexts.courses.domain.course_repository import CourseRepository
from src.contexts.courses.domain.errors.course_not_found import CourseNotFound
from src.contexts.shared.domain.value_objects.course_id import CourseId


class CourseFinder:
    def __init__(self, repository: CourseRepository) -> None:
        self.repository = repository

    def execute(self, course_id: CourseId) -> Course:
        course = self.repository.find_one(course_id.value)
        if not course:
            raise CourseNotFound(course_id.value)
        return course
