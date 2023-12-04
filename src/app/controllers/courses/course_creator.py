from uuid import uuid4

from dependency_injector.wiring import inject, Provide

from src.app.controllers.controller import ControllerInterfaz
from src.app.injections.containers import Containers
from src.contexts.courses.application.create.course_creator import CourseCreator
from src.contexts.courses.domain.course import Course


class CreateCourseController(ControllerInterfaz):

    @inject
    def __init__(self, use_case: CourseCreator = Provide[Containers.course_creator]) -> None:
        self.use_case = use_case

    def execute(self, request) -> Course:
        title = request.json.get("title")
        duration = request.json.get("duration")
        course = self.use_case.execute(str(uuid4()), title, duration)
        return course
