class CourseAlreadyExits(Exception):
    def __init__(self):
        super().__init__("Course with this title already exits.")
