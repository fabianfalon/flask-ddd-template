

class StringValueObject:
    value: str

    def __init__(self, value):
        self._validate_is_string(value)
        # The assignment of value is commented so that it
        # is carried out in each implementation
        # self.value = value

    @staticmethod
    def _validate_is_string(value):
        if not isinstance(value, str):
            raise ValueError("Value must be a string")
