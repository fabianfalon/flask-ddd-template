from uuid import uuid4

from src.app.controllers.controller import ControllerInterfaz
from src.contexts.courses.application.create.course_creator import CourseCreator
from src.contexts.courses.domain.course import Course
from src.contexts.courses.infrastructure.storage.mongo import MongoRepository
from src.contexts.shared.infrastructure.eventbus.in_memory_event_bus import InMemoryEventBus


class CreateCourseController(ControllerInterfaz):

    def __int__(self, repository, event_bus):
        self.__repository = repository
        self.__event_bus = event_bus

    def execute(self, request) -> Course:
        title = request.json.get("title")
        duration = request.json.get("duration")
        course = CourseCreator(
            repository=self.__repository,
            event_bus=self.__event_bus
        ).execute(str(uuid4()), title, duration)
        return course
