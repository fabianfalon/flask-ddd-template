

class Criteria:

    def __init__(
            self,
            filters=None,
            order=None,
            limit=None,
    ):
        self.filters = filters
        self.order = order
        self.limit = limit
