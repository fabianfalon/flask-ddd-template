from src.app.controllers.controller import ControllerInterfaz
from src.contexts.courses.application.create.course_get_all import CourseGetAll
from src.contexts.courses.domain.course import Course
from src.contexts.courses.infrastructure.storage.mongo import MongoRepository


class GetCourseController(ControllerInterfaz):
    def execute(self) -> Course:
        course = CourseGetAll(repository=MongoRepository()).execute()
        return course
