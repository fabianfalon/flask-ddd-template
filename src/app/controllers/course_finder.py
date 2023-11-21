from src.app.controllers.controller import ControllerInterfaz
from src.contexts.courses.application.finder.course_finder import CourseFinder
from src.contexts.courses.domain.course import Course
from src.contexts.courses.infrastructure.storage.mongo import MongoRepository


class CourseFinderController(ControllerInterfaz):
    def execute(self, request) -> Course:
        title = request.json.get("title")
        try:
            course = CourseFinder(repository=MongoRepository()).execute(title)
        except Exception as error:
            return None
        return course
