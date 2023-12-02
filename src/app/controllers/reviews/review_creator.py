from uuid import uuid4

from dependency_injector.wiring import inject, Provide

from src.app.controllers.controller import ControllerInterfaz
from src.app.injections.containers import Containers
from src.contexts.reviews.application.create.review_creator import ReviewCreator
from src.contexts.reviews.domain.review import Review


class CreateReviewController(ControllerInterfaz):

    @inject
    def __init__(
        self,
        review_creator: ReviewCreator = Provide[Containers.review_creator]
    ) -> None:
        self.review_creator = review_creator

    def execute(self, request, course_id) -> Review:
        comment = request.json.get("comment")
        review = self.review_creator.execute(str(uuid4()), course_id, comment)
        return review
