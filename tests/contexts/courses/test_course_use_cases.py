from uuid import uuid4

import pytest

from src.contexts.courses.application.create.course_creator import CourseCreator
from src.contexts.courses.application.find.course_finder import CourseFinder
from src.contexts.courses.domain.errors.course_already_exists import CourseAlreadyExits
from src.contexts.courses.domain.errors.course_not_found import CourseNotFound
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
    assert course.title == "test"
    assert course.duration == 60


@pytest.mark.parametrize("invalid_value", ["22", -1, 101])
def test_create_new_course_with_invalid_duration(invalid_value):
    repository = InMemoryRepository()
    repository.clear()
    with pytest.raises(ValueError):
        CourseCreator(repository).execute(
            CourseId(str(uuid4())), CourseTitle("test"), CourseDuration(invalid_value)
        )


@pytest.mark.parametrize("invalid_value", ["", None, 101])
def test_create_new_course_with_invalid_title(invalid_value):
    repository = InMemoryRepository()
    repository.clear()
    with pytest.raises(ValueError):
        CourseCreator(repository).execute(
            CourseId(str(uuid4())), CourseTitle(invalid_value), CourseDuration(60)
        )


def test_list_courses_ko():
    repository = InMemoryRepository()
    repository.clear()
    with pytest.raises(CourseNotFound):
        CourseFinder(repository).execute(CourseTitle("test"))


def test_should_raise_error_when_title_already_exists():
    repository = InMemoryRepository()
    repository.clear()
    CourseCreator(repository).execute(
        CourseId(str(uuid4())), CourseTitle("test"), CourseDuration(60)
    )
    with pytest.raises(CourseAlreadyExits):
        CourseCreator(repository).execute(
            CourseId(str(uuid4())), CourseTitle("test"), CourseDuration(60)
        )
