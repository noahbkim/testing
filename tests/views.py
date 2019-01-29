from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, "tests/index.html")


@login_required
def results(request):
    return render(request, "tests/results.html")


@login_required
def test(request, name):
    """"""
