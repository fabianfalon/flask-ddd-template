from bson.objectid import ObjectId
from src.contexts.reviews.domain.review import Review
from src.contexts.reviews.domain.review_repository import ReviewRepository
from src.contexts.shared.domain.value_objects.course_id import CourseId
from src.contexts.shared.infrastructure.storage.abstract_mongo_repository import AbstractMongoRepository

from typing import Dict, List, Optional


class MongoRepository(AbstractMongoRepository, ReviewRepository):

    def __init__(self) -> None:
        super().__init__()

    def collection_name(self):
        return "reviews"

    def find_one(self, review_id: str) -> Optional[Review]:
        review = self.database.get_collection(
            self.collection_name()
        ).find_one({"_id": ObjectId(review_id)})
        return self._create_review(review)

    def matching(self, criteria):
        ...

    def find_all(self) -> List[Review]:
        reviews = self.database.get_collection(
            self.collection_name()
        ).find()
        return [self._create_review(review) for review in reviews]

    def find_by_course_id(self, course_id: CourseId) -> Review:
        reviews = self.database.get_collection(
            self.collection_name()
        ).find({"course_id": course_id.value})
        return [self._create_review(review) for review in reviews]

    def update(self, review: Review) -> Optional[Review]:
        comment = review.to_primitive().get("comment")
        record = self.database.get_collection(
            self.collection_name()
        ).update_one(
            {"_id": ObjectId(review.id)},
            {
                "$set": {"comment": comment}
            },
            upsert=False,
        )
        return None if not self._create_review(record) else self.find_one(review.id)

    @staticmethod
    def _create_review(raw_data: Dict) -> Review:
        return Review.from_primitive(raw_data)
