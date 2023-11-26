from uuid import uuid4

from src.app.controllers.controller import ControllerInterfaz
from src.contexts.courses.application.find.course_finder import CourseFinder
from src.contexts.courses.infrastructure.storage.mongo import MongoRepository as CourseRepository
from src.contexts.reviews.application.create.review_creator import ReviewCreator
from src.contexts.reviews.domain.review import Review
from src.contexts.reviews.domain.value_objects.review_comment import ReviewComment
from src.contexts.reviews.domain.value_objects.review_id import ReviewId
from src.contexts.reviews.infrastructure.storage.mongo import MongoRepository as ReviewRepository
from src.contexts.shared.domain.value_objects.course_id import CourseId


class CreateReviewController(ControllerInterfaz):
    def execute(self, request, course_id) -> Review:
        comment = request.json.get("comment")
        finder = CourseFinder(repository=CourseRepository())
        review = ReviewCreator(repository=ReviewRepository(), finder=finder).execute(
            ReviewId(str(uuid4())), CourseId(course_id), ReviewComment(comment)
        )
        return review
