from src.app.controllers.controller import ControllerInterfaz
from src.contexts.courses.application.create.course_creator import CourseCreator
from src.contexts.courses.domain.course import Course
from src.contexts.courses.infrastructure.storage.in_memory import InMemoryRepository


class CreateCourseController(ControllerInterfaz):
    def execute(self, request) -> Course:
        title = request.json.get("title")
        duration = request.json.get("duration")
        course = CourseCreator(repository=InMemoryRepository()).execute(title, duration)
        return course
