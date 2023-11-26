from uuid import uuid4

from src.app.controllers.controller import ControllerInterfaz
from src.contexts.courses.application.create.course_creator import CourseCreator
from src.contexts.courses.domain.course import Course
from src.contexts.courses.domain.value_objects.course_duration import CourseDuration
from src.contexts.courses.domain.value_objects.course_title import CourseTitle
from src.contexts.courses.infrastructure.storage.mongo import MongoRepository
from src.contexts.shared.domain.value_objects.course_id import CourseId


class CreateCourseController(ControllerInterfaz):
    def execute(self, request) -> Course:
        title = request.json.get("title")
        duration = request.json.get("duration")
        course = CourseCreator(repository=MongoRepository()).execute(
            CourseId(str(uuid4())), CourseTitle(title), CourseDuration(duration)
        )
        return course
