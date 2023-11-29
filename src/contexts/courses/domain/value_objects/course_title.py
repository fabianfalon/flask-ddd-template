from src.contexts.shared.domain.value_objects.string_value_object import StringValueObject


class CourseTitle(StringValueObject):
    value: str

    def __init__(self, value):
        super().__init__(value)
        self._validate_is_valid_title(value)
        self.value = value

    @staticmethod
    def _validate_is_valid_title(value):
        if len(value) <= 0:
            raise ValueError("Title must not be empty.")
