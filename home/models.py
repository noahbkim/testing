from django.db import models
from django.contrib.auth.models import User
from enum import Enum, IntEnum


class SEX(Enum):
    """Sex field options. Boolean is space efficient."""

    MALE = False
    FEMALE = True


class PROSOPAGNOSIA(IntEnum):
    """Prosopagnosia classifications. Average means has prosopagnosia."""

    CONTROL = 0
    AVERAGE = 1
    EXTREME = 2


class Subject(models.Model):
    """A profile linked to users who register as subjects."""

    # Link to the user
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Track a couple other details
    semester = models.CharField(max_length=5)  # Formatted YYYYS where S can be 1 or 2
    birthday = models.DateField()
    sex = models.BooleanField()
    prosopagnosia = models.PositiveSmallIntegerField(choices=((item, item.value) for item in PROSOPAGNOSIA))

    # Email confirmation
    token = models.CharField(max_length=32)
    confirmed = models.BooleanField(default=False)
