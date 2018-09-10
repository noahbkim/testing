from django.urls import path

from . import views


app_name = "tests"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.test, name="test")
]
