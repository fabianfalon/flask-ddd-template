
import pymongo
from bson.objectid import ObjectId
from src.contexts.courses.domain.course import Course
from src.contexts.courses.domain.course_repository import CourseRepository
from src.contexts.shared.infrastructure.storage.abstract_mongo_repository import AbstractMongoRepository

from typing import Dict, List, NoReturn, Optional


class MongoRepository(AbstractMongoRepository, CourseRepository):
    def __init__(self) -> None:
        super().__init__()

    def collection_name(self):
        return "courses"

    def delete(self, course_id: str) -> NoReturn:
        self.database.get_collection(
            self.collection_name()
        ).delete_one({"_id": ObjectId(course_id)})

    def find_one(self, course_id: str) -> Optional[Course]:
        course = self.database.get_collection(
            self.collection_name()
        ).find_one({"course_id": course_id})
        if course:
            return self._create_course(course)
        return None

    def find_all(self) -> List[Course]:
        courses = self.database.get_collection(
            self.collection_name()
        ).find()
        return [self._create_course(course) for course in courses]

    def matching(self, criteria):
        ...

    def find_one_by_title(self, title):
        course = self.database.get_collection(
            self.collection_name()
        ).find_one({"title": title})
        if course:
            return self._create_course(course)
        return None

    def update(self, course: Course) -> Optional[Course]:
        course_dict = course.to_primitive()
        record = self.database.course.update_one(
            {"_id": ObjectId(course_dict.get("id"))},
            {
                "$set": {
                    "title": course_dict.get("title"),
                    "duration": course_dict.get("duration"),
                }
            },
            upsert=True,
        )
        return None if not self._create_course(record) else self.find_one(course.id)

    @staticmethod
    def _create_course(raw_data: Dict) -> Course:
        return Course.from_primitive(raw_data)
