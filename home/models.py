from django.db import models
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

    semester = models.CharField(max_length=5)  # Formatted YYYYS where S can be 1 or 2
    birthday = models.DateField()
    sex = models.BooleanField()
    prosopagnosia = models.PositiveSmallIntegerField(choices=((item, item.value) for item in PROSOPAGNOSIA))
