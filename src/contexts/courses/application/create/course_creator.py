from src.contexts.courses.domain.course import Course
from src.contexts.courses.domain.course_repository import CourseRepository
from src.contexts.courses.domain.errors.course_already_exists import CourseAlreadyExits
from src.contexts.courses.domain.value_objects.course_title import CourseTitle
from src.contexts.shared.domain.event_bus import EventBus


class CourseCreator:
    def __init__(self, repository: CourseRepository, event_bus: EventBus) -> None:
        self.repository = repository
        self.__event_bus = event_bus

    def execute(self, course_id: str, title: str, duration: float):
        recorded = self.repository.find_one_by_title(CourseTitle(title).value.lower().strip())
        if recorded:
            raise CourseAlreadyExits()

        course = Course.create(course_id, title, duration)
        self.repository.save(course)
        self.__event_bus.publish(course.pull_domain_events())
        return course
