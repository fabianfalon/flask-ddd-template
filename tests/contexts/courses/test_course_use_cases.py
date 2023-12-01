from uuid import uuid4

import pytest

from src.contexts.courses.application.create.course_creator import CourseCreator
from src.contexts.courses.application.find.course_finder import CourseFinder
from src.contexts.courses.domain.errors.course_already_exists import CourseAlreadyExits
from src.contexts.courses.domain.errors.course_not_found import CourseNotFound
from src.contexts.courses.infrastructure.storage.in_memory import InMemoryRepository
from src.contexts.shared.infrastructure.eventbus.in_memory_event_bus import InMemoryEventBus


def test_create_new_course():
    repository = InMemoryRepository()
    event_bus = InMemoryEventBus()
    repository.clear()
    course = CourseCreator(
        repository, event_bus
    ).execute(str(uuid4()), "test", 60)
    assert course.title == "test"
    assert course.duration == 60


@pytest.mark.parametrize("invalid_value", ["22", -1, 101])
def test_create_new_course_with_invalid_duration(invalid_value):
    repository = InMemoryRepository()
    event_bus = InMemoryEventBus()

    repository.clear()
    with pytest.raises(ValueError):
        CourseCreator(
            repository,
            event_bus
        ).execute(str(uuid4()), "test", invalid_value)


@pytest.mark.parametrize("invalid_value", ["", None, 101])
def test_create_new_course_with_invalid_title(invalid_value):
    event_bus = InMemoryEventBus()
    repository = InMemoryRepository()
    repository.clear()
    with pytest.raises(ValueError):
        CourseCreator(
            repository,
            event_bus
        ).execute(str(uuid4()), invalid_value, 60)


def test_list_courses_ko():
    repository = InMemoryRepository()
    repository.clear()
    with pytest.raises(CourseNotFound):
        CourseFinder(repository).execute("test")


def test_should_raise_error_when_title_already_exists():
    event_bus = InMemoryEventBus()
    repository = InMemoryRepository()
    repository.clear()
    course_creator = CourseCreator(repository, event_bus)
    course_creator.execute(str(uuid4()), "test", 60)
    with pytest.raises(CourseAlreadyExits):
        course_creator.execute(str(uuid4()), "test", 60)
