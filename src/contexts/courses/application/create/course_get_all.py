from typing import List

from src.contexts.courses.domain.course import Course
from src.contexts.courses.domain.course_repository import CourseRepository


class CourseGetAll:
    def __init__(self, repository: CourseRepository) -> None:
        self.repository = repository

    def execute(self, request) -> List[Course]:
        courses = self.repository.find_all()
        return courses
