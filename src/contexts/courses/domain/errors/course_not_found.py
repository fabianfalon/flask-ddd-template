class CourseNotFound(Exception):
    def __init__(self, title: str):
        super().__init__(f"Course with title {title} not found.")
        self.title = title
