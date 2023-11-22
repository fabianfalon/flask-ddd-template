class CourseNotFound(Exception):
    def __init__(self, title: str):
        super().__init__(f"Course with id {title} not found.")
        self.title = title
