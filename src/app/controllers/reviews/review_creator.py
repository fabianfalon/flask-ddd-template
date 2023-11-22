from src.app.controllers.controller import ControllerInterfaz
from src.contexts.reviews.application.create.review_creator import ReviewCreator
from src.contexts.reviews.domain.review import Review
from src.contexts.reviews.infrastructure.storage.mongo import MongoRepository as ReviewRepository

from src.contexts.courses.application.find.course_finder import CourseFinder
from src.contexts.courses.infrastructure.storage.mongo import MongoRepository as CourseRepository


class CreateReviewController(ControllerInterfaz):
    def execute(self, request, course_id) -> Review:
        comment = request.json.get("comment")
        finder = CourseFinder(repository=CourseRepository())
        try:
            review = ReviewCreator(
                repository=ReviewRepository(), finder=finder
            ).execute(course_id, comment)
        except Exception as error:
            return error
        return review
