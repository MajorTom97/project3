from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', views.index, name='index'),
    path("register/", views.register, name="register"),
    path('menu/', views.Menu, name="menu"),
    path('cart/', views.cart, name="cart"),
    path('history/', views.history, name="history"),
    path('buy/', views.buy, name="buy")
]