from src.app.controllers.controller import ControllerInterfaz
from src.contexts.reviews.application.find.review_get_all import ReviewGetAllByCourse
from src.contexts.reviews.domain.review import Review
from src.contexts.reviews.infrastructure.storage.mongo import MongoRepository
from src.contexts.shared.domain.value_objects.course_id import CourseId


class ListReviewByCourseController(ControllerInterfaz):
    def execute(self, course_id) -> Review:
        try:
            review = ReviewGetAllByCourse(repository=MongoRepository()).execute(CourseId(course_id))
        except Exception as error:
            return error
        return review
