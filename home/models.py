from django.db import models
from django.contrib.auth.models import User
import enum
import random


class SEX(enum.Enum):
    """Sex field options. Boolean is space efficient."""

    MALE = False
    FEMALE = True


class PROSOPAGNOSIA(enum.IntEnum):
    """Prosopagnosia classifications. Average means has prosopagnosia."""

    CONTROL = 0
    AVERAGE = 1
    EXTREME = 2


HEX = "0123456789abcdef"

TOKEN_LENGTH = 48


class Subject(models.Model):
    """A profile linked to users who register as subjects."""

    # Link to the user
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="subject")

    # Track a couple other details
    semester = models.CharField(max_length=5)  # Formatted YYYYS where S can be 1 or 2
    age = models.IntegerField()
    sex = models.BooleanField()

    # Email confirmation
    token = models.CharField(max_length=TOKEN_LENGTH, unique=True)
    confirmed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        """Called when the object is saved."""

        # If this is a new object generate a confirmation token
        if self.pk is None:
            token = None
            while token is None:
                test = "".join(random.choice(HEX) for _ in range(TOKEN_LENGTH))
                if not Subject.objects.filter(token=test).exists():
                    token = test
            self.token = token

        super().save(*args, **kwargs)
