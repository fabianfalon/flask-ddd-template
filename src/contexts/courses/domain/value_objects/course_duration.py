class CourseDuration:
    value: str

    def __init__(self, value):
        self._validate_is_valid_duration(value)
        self.value = value

    @staticmethod
    def _validate_is_valid_duration(value):
        if isinstance(value, str):
            raise ValueError("Course duration must be a number.")
        if value <= 0 or value > 100:
            raise ValueError("Course duration must be between 0 and 100.")
