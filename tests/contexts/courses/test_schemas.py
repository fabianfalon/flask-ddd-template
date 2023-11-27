from uuid import uuid4

from src.contexts.courses.application.create.course_creator import CourseCreator
from src.contexts.courses.application.create.course_get_all import CourseGetAll
from src.contexts.courses.infrastructure.serializers import CourseSchema
from src.contexts.courses.infrastructure.storage.in_memory import InMemoryRepository


def test_create_new_course():
    repository = InMemoryRepository()
    repository.clear()
    course = CourseCreator(repository).execute(str(uuid4()), "test", 60)
    schema = CourseSchema().dump(course, many=False)
    assert schema.get("title") == "test"
    assert schema.get("duration") == 60


def test_list_courses():
    repository = InMemoryRepository()
    repository.clear()
    CourseCreator(repository).execute(str(uuid4()), "test1", 60)
    CourseCreator(repository).execute(str(uuid4()), "test2", 60)
    CourseCreator(repository).execute(str(uuid4()), "test3", 60)

    courses = CourseGetAll(repository).execute()
    schemas = CourseSchema(many=True).dump(list(courses))
    assert len(schemas) == 3
