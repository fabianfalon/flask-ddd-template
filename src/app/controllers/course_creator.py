from src.app.controllers.controller import ControllerInterfaz
from src.contexts.courses.application.create.course_creator import CourseCreator
from src.contexts.courses.domain.course import Course
from src.contexts.courses.infrastructure.storage.mongo import MongoRepository


class CreateCourseController(ControllerInterfaz):
    def execute(self, request) -> Course:
        title = request.json.get("title")
        duration = request.json.get("duration")
        course = CourseCreator(repository=MongoRepository()).execute(title, duration)
        return course
