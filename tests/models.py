from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.utils import timezone

import string

from testing import settings


def validate_alphanumeric(test):
    """The name of a test must be alphanumeric with underscores."""

    if any(c not in string.ascii_letters + string.digits + "_" for c in test):
        raise ValidationError("name may only contains letters, digits, and underscores")


class Test(models.Model):
    """Contains relevant information about subject tests."""

    # A short, human readable name for use in data output and URLs
    name = models.CharField(max_length=8, unique=True, validators=[validate_alphanumeric])

    # The full title of the test
    title = models.CharField(max_length=64)

    # The CSV file containing the test data
    file = models.FileField(upload_to=settings.TESTS_ROOT)


class Result(models.Model):
    """The result of a test taken by a single subject."""

    # The user who took the test
    user = models.ForeignKey(User, related_name="results", on_delete=models.CASCADE)

    # The test that was taken
    test = models.ForeignKey(Test, related_name="results", on_delete=models.CASCADE)

    # When the test was taken
    date_taken = models.DateTimeField(default=timezone.now)
