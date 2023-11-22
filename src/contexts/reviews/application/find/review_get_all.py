from src.contexts.reviews.domain.review_repository import ReviewRepository


class ReviewGetAllByCourse:
    def __init__(self, repository: ReviewRepository) -> None:
        self.repository = repository

    def execute(self, course_id):
        reviews = self.repository.find_one_by_course_id(course_id)
        return reviews
