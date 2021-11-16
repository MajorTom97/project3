from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings

urlpatterns = [
    path("", views.index, name="index"),
    path("signin", LoginView.as_view(template_name="signin.html"), name="signin"),
    path("signout", LogoutView.as_view(template_name="signout.html"), name="signout"),
    path("register", view.register(template_name="register.html"), name="register"),
]
