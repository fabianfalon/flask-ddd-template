from src.app.controllers.controller import ControllerInterfaz
from src.contexts.reviews.application.create.review_creator import ReviewCreator
from src.contexts.reviews.domain.review import Review
from src.contexts.reviews.infrastructure.storage.mongo import MongoRepository


class CreateReviewController(ControllerInterfaz):
    def execute(self, request, course_id) -> Review:
        comment = request.json.get("comment")
        review = ReviewCreator(repository=MongoRepository()).execute(course_id, comment)
        return review
