from django.db import models
from django.contrib.auth.models import User
from enum import Enum, IntEnum
import random


class SEX(Enum):
    """Sex field options. Boolean is space efficient."""

    MALE = False
    FEMALE = True


class PROSOPAGNOSIA(IntEnum):
    """Prosopagnosia classifications. Average means has prosopagnosia."""

    CONTROL = 0
    AVERAGE = 1
    EXTREME = 2


HEX = "0123456789abcdef"


class Subject(models.Model):
    """A profile linked to users who register as subjects."""

    # Link to the user
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="subject")

    # Track a couple other details
    semester = models.CharField(max_length=5)  # Formatted YYYYS where S can be 1 or 2
    age = models.IntegerField()
    sex = models.BooleanField()

    # Whether they have prosopagnosia
    prosopagnosia = models.PositiveSmallIntegerField(choices=((item, item.value) for item in PROSOPAGNOSIA), null=True)

    # Email confirmation
    token = models.CharField(max_length=24, unique=True)
    confirmed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        """Called when the object is saved."""

        # If this is a new object generate a confirmation token
        if self.pk is None:
            token = None
            while token is None:
                test = "".join(random.choice(HEX) for _ in range(24))
                if not Subject.objects.filter(token=test).exists():
                    token = test
            self.token = token

        super().save(*args, **kwargs)
