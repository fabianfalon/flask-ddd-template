from src.app.controllers.controller import ControllerInterfaz
from src.contexts.courses.application.find.course_finder import CourseFinder
from src.contexts.courses.domain.course import Course
from src.contexts.courses.infrastructure.storage.mongo import MongoRepository


class CourseFinderController(ControllerInterfaz):
    def execute(self, course_id) -> Course:
        try:
            course = CourseFinder(repository=MongoRepository()).execute(course_id)
        except Exception as error:
            return None
        return course
