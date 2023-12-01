from uuid import uuid4

from src.contexts.courses.application.create.course_creator import CourseCreator
from src.contexts.courses.application.create.course_get_all import CourseGetAll
from src.contexts.courses.infrastructure.serializers import CourseSchema
from src.contexts.courses.infrastructure.storage.in_memory import InMemoryRepository
from src.contexts.shared.infrastructure.eventbus.in_memory_event_bus import InMemoryEventBus


def test_create_new_course():
    event_bus = InMemoryEventBus()

    repository = InMemoryRepository()
    repository.clear()
    course = CourseCreator(repository, event_bus).execute(str(uuid4()), "test", 60)
    schema = CourseSchema().dump(course, many=False)
    assert schema.get("title") == "test"
    assert schema.get("duration") == 60


def test_list_courses():
    event_bus = InMemoryEventBus()

    repository = InMemoryRepository()
    repository.clear()
    course_creator = CourseCreator(
        repository, event_bus
    )
    course_creator.execute(str(uuid4()), "test1", 60)
    course_creator.execute(str(uuid4()), "test2", 60)
    course_creator.execute(str(uuid4()), "test3", 60)

    courses = CourseGetAll(repository).execute()
    schemas = CourseSchema(many=True).dump(list(courses))
    assert len(schemas) == 3
