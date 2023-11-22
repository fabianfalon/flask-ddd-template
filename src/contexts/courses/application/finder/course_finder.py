from src.contexts.courses.domain.course import Course
from src.contexts.courses.domain.course_repository import CourseRepository
from src.contexts.courses.domain.errors.course_not_found import CourseNotFound


class CourseFinder:
    def __init__(self, repository: CourseRepository) -> None:
        self.repository = repository

    def execute(self, title: str) -> Course:
        course = self.repository.find_one_by_title(title.lower().strip())
        if not course:
            raise CourseNotFound(title)
        return course
