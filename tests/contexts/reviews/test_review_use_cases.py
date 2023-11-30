from uuid import uuid4

from src.contexts.reviews.application.create.review_creator import ReviewCreator
from src.contexts.reviews.application.find.review_get_all import ReviewGetAllByCourse
from src.contexts.reviews.infrastructure.storage.in_memory import InMemoryReviewRepository

from src.contexts.courses.application.create.course_creator import CourseCreator
from src.contexts.courses.infrastructure.storage.in_memory import InMemoryRepository as InMemoryCourseRepository
from src.contexts.courses.application.find.course_finder import CourseFinder


def test_create_new_review_ok():
    course_repository = InMemoryCourseRepository()
    course_repository.clear()
    course = CourseCreator(course_repository).execute(str(uuid4()), "test", 60)

    finder = CourseFinder(course_repository)
    review_repository = InMemoryReviewRepository()
    review_repository.clear()
    review_uuid = str(uuid4())
    review_comment = "comentario de prueba"

    review = ReviewCreator(review_repository, finder).execute(
        review_uuid,  course.id,  review_comment
    )
    assert review.review_id == review_uuid
    assert review.comment == review_comment


def test_get_review_list_ok():
    course_repository = InMemoryCourseRepository()
    course_repository.clear()
    course = CourseCreator(course_repository).execute(str(uuid4()), "test", 60)

    finder = CourseFinder(course_repository)
    review_repository = InMemoryReviewRepository()
    review_repository.clear()

    for i in range(3):
        review_uuid = str(uuid4())
        review_comment = f"comentario de prueba {i}"
        ReviewCreator(review_repository, finder).execute(
            review_uuid,  course.id,  review_comment
        )
    reviews = ReviewGetAllByCourse(review_repository).execute(course.id)
    assert len(reviews) == 3
