from src.contexts.courses.domain.course import Course
from src.contexts.courses.domain.course_repository import CourseRepository
from src.contexts.courses.domain.errors.course_already_exists import CourseAlreadyExits
from src.contexts.courses.domain.value_objects.course_duration import CourseDuration
from src.contexts.courses.domain.value_objects.course_title import CourseTitle
from src.contexts.shared.domain.value_objects.course_id import CourseId


class CourseCreator:
    def __init__(self, repository: CourseRepository) -> None:
        self.repository = repository

    def execute(self, course_id: CourseId, title: CourseTitle, duration: CourseDuration):
        recorded = self.repository.find_one_by_title(title.value.lower().strip())
        if recorded:
            raise CourseAlreadyExits()

        course = Course(course_id.value, title.value, duration.value, None, None)
        self.repository.save(course)
        return course
