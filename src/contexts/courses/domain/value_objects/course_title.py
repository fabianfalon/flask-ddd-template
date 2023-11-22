class CourseTitle:
    value: str

    def __init__(self, value):
        self._validate_is_valid_title(value)
        self.value = value

    @staticmethod
    def _validate_is_valid_title(value):
        if not isinstance(value, str):
            raise ValueError("Title must be a string.")
        if len(value) <= 0:
            raise ValueError("Title must not be empty.")
