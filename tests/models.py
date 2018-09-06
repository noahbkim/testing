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


"""Example test file

meta:
  name: dopp
  title: Doppelganger Accuracy Test
  templates: 
    rate: templates/rate.html
    
slides:
- tom_cruise
  template: rate
  image1: test/tom_cruise.png
  image2: test/not_tom_cruise.png
  correct: 
  inputs: 
    - Left
    - Right
    
rate.html:
<styles>
    ....
</styles>
<img src="%image2%">
<img src="%image2%">


Use an actual IFrame to embed each new test, let the IFrame redirect itself.
Serve the pages to randomly generated URL which is requested by the client and posted to the IFrame.
Each test page is provided the arguments from the URL, namely the slide name.
The information is taken from an in-memory copy of the imported test and the page is generated.

Need to test performance!
"""
