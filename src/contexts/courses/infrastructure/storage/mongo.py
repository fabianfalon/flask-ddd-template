import os

import pymongo
from bson.objectid import ObjectId
from src.contexts.courses.domain.course import Course
from src.contexts.courses.domain.course_repository import CourseRepository

from typing import Dict, List, NoReturn, Optional

MONGO_URL = os.environ.get("MONGO_URL", "mongodb://127.0.0.1:27017/courses")


class MongoRepository(CourseRepository):
    def __init__(self) -> None:
        client = pymongo.MongoClient(MONGO_URL)
        self.database = client.courses

    def save(self, course: Course) -> Course:
        self.database.courses.insert_one(
            {
                "course_id": course.id,
                "title": course.title,
                "duration": course.duration,
                "created_at": course.created_at,
                "updated_at": course.updated_at,
            }
        )

    def delete(self, course_id: str) -> NoReturn:
        self.database.courses.delete_one({"_id": ObjectId(course_id)})

    def find_one(self, course_id: str) -> Optional[Course]:
        course = self.database.courses.find_one({"course_id": course_id})
        if course:
            return self._create_course(course)
        return None

    def find_all(self) -> List[Course]:
        courses = self.database.courses.find()
        return [self._create_course(course) for course in courses]

    def matching(self, criteria):
        ...

    def find_one_by_title(self, title):
        course = self.database.courses.find_one({"title": title})
        if course:
            return self._create_course(course)
        return None

    def update(self, course: Course) -> Optional[Course]:
        record = self.database.course.update_one(
            {"_id": ObjectId(course.id)},
            {
                "$set": {
                    "title": course.title,
                    "duration": course.duration,
                }
            },
            upsert=False,
        )
        return None if not record else self.find(course.id)

    @staticmethod
    def _create_course(course: Dict) -> Course:
        return Course(
            course_id=str(course.get("_id")),
            title=course.get("title"),
            duration=float(course.get("duration")),
            created_at=course.get("created_at"),
            updated_at=course.get("updated_at"),
        )
