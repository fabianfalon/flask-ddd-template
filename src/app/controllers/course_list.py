from src.app.controllers.controller import ControllerInterfaz
from src.contexts.courses.application.create.course_get_all import CourseGetAll
from src.contexts.courses.domain.course import Course
from src.contexts.courses.infrastructure.storage.in_memory import InMemoryRepository


class GetCourseController(ControllerInterfaz):
    def execute(self) -> Course:
        course = CourseGetAll(repository=InMemoryRepository()).execute()
        return course
