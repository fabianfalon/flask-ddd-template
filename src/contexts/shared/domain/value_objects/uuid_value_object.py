from dataclasses import dataclass


@dataclass(frozen=True)
class UUIDValue:
    value: str
