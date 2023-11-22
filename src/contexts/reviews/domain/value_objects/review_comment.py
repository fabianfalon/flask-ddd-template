class ReviewComment:
    value: str

    def __init__(self, value):
        self._validate_is_valid_comment(value)
        self.value = value

    @staticmethod
    def _validate_is_valid_comment(value):
        if not isinstance(value, str):
            raise ValueError("Comment must be a string.")
        if len(value) <= 0:
            raise ValueError("Comment must not be empty.")
