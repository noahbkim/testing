from django.db import models
from django.contrib.auth.models import User

from . import identifier


class IdentifierField(models.CharField):
    """A field for a unique identifier."""

    def __init__(self, **kwargs):
        """Initialize a new identifier field."""

        kwargs["max_length"] = identifier.IDENTIFIER_LENGTH
        kwargs["unique"] = True
        super().__init__(**kwargs)


def generate_identifier(user: User) -> str:
    """Generate an identifier from a Django user model"""

    yield from identifier.generate_identifier()

