from src.app.controllers.controller import ControllerInterfaz
from src.contexts.reviews.application.find.review_get_all import ReviewGetAllByCourse
from src.contexts.reviews.domain.review import Review
from src.contexts.reviews.domain.review_repository import ReviewRepository


class ListReviewByCourseController(ControllerInterfaz):
    def __init__(self, repository: ReviewRepository, event_bus) -> None:
        self.__repository = repository
        self.__event_bus = event_bus

    def execute(self, course_id) -> Review:
        try:
            review = ReviewGetAllByCourse(repository=self.__repository).execute(course_id)
        except Exception as error:
            return error
        return review
