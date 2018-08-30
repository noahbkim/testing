from django.shortcuts import render


def index(request):
    """Render the home page of the website."""

    return render(request, "home/index.html")
