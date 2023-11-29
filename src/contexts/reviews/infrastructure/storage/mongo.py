import os

import pymongo
from bson.objectid import ObjectId
from src.contexts.reviews.domain.review import Review
from src.contexts.reviews.domain.review_repository import ReviewRepository
from src.contexts.shared.domain.value_objects.course_id import CourseId

from typing import Dict, List, NoReturn, Optional

MONGO_URL = os.environ.get("MONGO_URL", "mongodb://127.0.0.1:27017/courses")


class MongoRepository(ReviewRepository):
    def __init__(self) -> None:
        client = pymongo.MongoClient(MONGO_URL)
        self.database = client.courses

    def save(self, aggregate_root: Review) -> Review:
        self.database.reviews.insert_one(aggregate_root.to_primitive())

    def delete(self, review_id: str) -> NoReturn:
        pass

    def find_one(self, review_id: str) -> Optional[Review]:
        ...

    def find_all(self) -> List[Review]:
        reviews = self.database.reviews.find()
        return [self._create_review(review) for review in reviews]

    def matching(self, criteria):
        ...

    def find_by_course_id(self, course_id: CourseId) -> Review:
        reviews = self.database.reviews.find({"course_id": course_id.value})
        return [self._create_review(review) for review in reviews]

    def update(self, review: Review) -> Optional[Review]:
        record = self.database.reviews.update_one(
            {"_id": ObjectId(review.id)},
            {
                "$set": {
                    "comment": review.comment,
                }
            },
            upsert=False,
        )
        return None if not record else self.find(review.id)

    @staticmethod
    def _create_review(raw_data: Dict) -> Review:
        return Review.from_primitive(raw_data)
