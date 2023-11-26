from uuid import uuid4

from src.contexts.courses.application.create.course_creator import CourseCreator
from src.contexts.courses.application.create.course_get_all import CourseGetAll
from src.contexts.courses.infrastructure.serializers import CourseSchema
from src.contexts.courses.infrastructure.storage.in_memory import InMemoryRepository
from src.contexts.courses.domain.value_objects.course_duration import CourseDuration
from src.contexts.shared.domain.value_objects.course_id import CourseId
from src.contexts.courses.domain.value_objects.course_title import CourseTitle


def test_create_new_course():
    repository = InMemoryRepository()
    repository.clear()
    course = CourseCreator(repository).execute(
        CourseId(str(uuid4())), CourseTitle("test"), CourseDuration(60)
    )
    schema = CourseSchema().dump(course, many=False)
    assert schema.get("title") == "test"
    assert schema.get("duration") == 60


def test_list_courses():
    repository = InMemoryRepository()
    repository.clear()
    CourseCreator(repository).execute(
        CourseId(str(uuid4())), CourseTitle("test1"), CourseDuration(60)
    )
    CourseCreator(repository).execute(
        CourseId(str(uuid4())), CourseTitle("test2"), CourseDuration(60)
    )
    CourseCreator(repository).execute(
        CourseId(str(uuid4())), CourseTitle("test3"), CourseDuration(60)
    )

    courses = CourseGetAll(repository).execute()
    schemas = CourseSchema(many=True).dump(list(courses))
    assert len(schemas) == 3


