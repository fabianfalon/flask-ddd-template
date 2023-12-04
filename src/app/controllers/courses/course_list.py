from dependency_injector.wiring import inject, Provide

from src.app.controllers.controller import ControllerInterfaz
from src.app.injections.containers import Containers
from src.contexts.courses.application.create.course_get_all import CourseGetAll
from src.contexts.courses.domain.course import Course


class GetCourseController(ControllerInterfaz):

    @inject
    def __init__(self, use_case: CourseGetAll = Provide[Containers.course_get_all]) -> None:
        self.use_case = use_case

    def execute(self, request) -> Course:
        course = self.use_case.execute(request)
        return course
