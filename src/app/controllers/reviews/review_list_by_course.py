from dependency_injector.wiring import Provide, inject

from src.app.controllers.controller import ControllerInterfaz
from src.app.injections.containers import Containers
from src.contexts.reviews.application.find.review_get_all import ReviewGetAllByCourse
from src.contexts.reviews.domain.review import Review


class ListReviewByCourseController(ControllerInterfaz):

    @inject
    def __init__(
        self,
        review_get_all_by_course: ReviewGetAllByCourse = Provide[Containers.review_get_all_by_course]
    ) -> None:
        self.review_get_all_by_course = review_get_all_by_course

    def execute(self, course_id) -> Review:
        try:
            review = self.review_get_all_by_course.execute(course_id)
        except Exception as error:
            return error
        return review
