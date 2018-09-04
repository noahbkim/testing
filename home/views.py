from django.shortcuts import render


def index(request):
    """Render the home page of the website."""

    return render(request, "home/index.html")


def register(request):
    """Register a subject for testing."""

    if request.method == "POST":
        



        return render(request, "home/done.html")

    return render(request, "home/register.html")
