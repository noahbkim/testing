from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.mail import send_mail

import os

from . import models
from . import forms
from testing import settings


with open(os.path.join(os.path.dirname(__file__), "mail", "confirmation.txt")) as file:
    CONFIRMATION = file.read()


def index(request):
    """Render the home page of the website."""

    return render(request, "home/index.html")


def about(request):
    return render(request, "home/about.html")


def instructions(request):
    return render(request, "home/instructions.html")


def contact(request):
    return render(request, "home/contact.html")


def register(request):
    """Register a subject for testing."""

    if request.method == "POST":

        # Check the form, complete if valid
        form = forms.SubjectForm(request.POST)
        if form.is_valid():

            # Create the user account and send the email
            user = User.objects.create_user(
                username=form.cleaned_data["email"],
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password1"])
            user.save()
            subject = models.Subject.objects.create(
                user=user,
                age=form.cleaned_data["age"],
                sex=bool(form.cleaned_data["sex"]))
            subject.save()

            # Send an email with the confirmation code
            send_mail(
                "USC Face Study confirmation",
                CONFIRMATION.format(name=user.first_name, url=settings.URL + "/" + subject.token),
                "face-study-no-reply@usc.edu",
                [user.email],
                fail_silently=False)

            return render(request, "home/done.html", {"email": user.email})

        # Collect all the errors for ease of access
        errors = []
        for field in form:
            for error in field.errors:
                errors.append(error)
        for error in form.non_field_errors():
            errors.append(error)

        # Render the invalid form
        return render(request, "home/register.html", {"errors": ", ".join(errors), "form": form})

    # Render the page with a blank form so the renderer isn't sad
    return render(request, "home/register.html", {"form": forms.SubjectForm()})


def confirm(request, token):
    """Confirm a user based on the code they've been sent via email."""

    subject = get_object_or_404(models.Subject, token=token)
    subject.confirmed = True
    subject.save()
    return render(request, "home/confirmed.html")


def login(request):
    """Standard login page."""

    if request.method == "POST":

        # Check if the user is valid
        user = auth.authenticate(username=request.POST["email"], password=request.POST["password"])
        if user is None:
            return render(request, "home/login.html", {"error": "invalid credentials!"})
        if hasattr(user, "subject") and not user.subject.confirmed:
            return render(request, "home/unconfirmed.html", {"email": user.email})
        auth.login(request, user)
        return redirect("home:index")

    return render(request, "home/login.html")


def logout(request):
    """Logout the user."""

    auth.logout(request)
    return redirect("home:index")
