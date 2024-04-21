"""
This module provides a mixin class for objects with an id field.
"""
from dataclasses import dataclass


class InvalidIdError(Exception):
    """Exception raised for invalid id values."""

    def __init__(self, id_value):
        self.id_value = id_value
        super().__init__(f"Id must be a positive integer. Got {id_value}.")


@dataclass()
class IdMixin:
    """Mixin class for objects with an id field."""
    id: int

    def __post_init__(self):
        if self.id < 0:
            raise InvalidIdError(self.id)
