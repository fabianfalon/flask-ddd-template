from src.contexts.courses.domain.course import Course
from src.contexts.courses.domain.course_repository import CourseRepository
from src.contexts.courses.domain.course_finder import CourseFinder as DomainCourseFinder
from src.contexts.shared.domain.value_objects.course_id import CourseId


class CourseFinder:
    def __init__(self, repository: CourseRepository) -> None:
        self.finder = DomainCourseFinder(repository)

    def execute(self, course_id: CourseId) -> Course:

        return self.finder.execute(course_id)
