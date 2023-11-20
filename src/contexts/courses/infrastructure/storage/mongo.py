from typing import List, NoReturn, Optional

from src.contexts.courses.domain.course import Course
from src.contexts.courses.domain.course_repository import CourseRepository


class MongoRepository(CourseRepository):
    def save(self, course: Course) -> Course:
        ...

    def delete(self, course_id: str) -> NoReturn:
        ...

    def find_one(self, course_id: str) -> Optional[Course]:
        ...

    def find_all(self) -> List[Course]:
        ...

    def matching(self, criteria):
        ...

    def find_one_by_title(self, title):
        ...
