from django.urls import path

from . import views


app_name = "home"

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("instructions", views.instructions, name="instructions"),
    path("contact", views.contact, name="contact"),
    path("register", views.register, name="register"),
    path("confirm/<str:token>", views.confirm, name="confirm"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
]
