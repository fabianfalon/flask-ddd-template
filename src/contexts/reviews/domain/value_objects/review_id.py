from dataclasses import dataclass


@dataclass(frozen=True)
class ReviewId:
    value: str
