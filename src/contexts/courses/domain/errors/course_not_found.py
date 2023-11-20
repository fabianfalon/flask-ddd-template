class CourseNotFound(Exception):
    def __init__(self, course_id: str):
        super().__init__(f"Course with ID {course_id} not found.")
        self.course_id = course_id
