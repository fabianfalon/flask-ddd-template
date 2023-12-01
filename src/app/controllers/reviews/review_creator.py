from uuid import uuid4

from src.app.controllers.controller import ControllerInterfaz
from src.contexts.courses.application.find.course_finder import CourseFinder
from src.contexts.reviews.application.create.review_creator import ReviewCreator
from src.contexts.reviews.domain.review import Review
from src.contexts.reviews.domain.review_repository import ReviewRepository


class CreateReviewController(ControllerInterfaz):

    def __init__(self, repository: ReviewRepository, finder: CourseFinder) -> None:
        self.__repository = repository
        self.__finder = finder

    def execute(self, request, course_id) -> Review:
        comment = request.json.get("comment")
        review = ReviewCreator(repository=self.__repository, finder=self.__finder).execute(
            str(uuid4()), course_id, comment
        )
        return review
