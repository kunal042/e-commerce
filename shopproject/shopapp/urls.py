from django.urls import path
from shopapp import views

urlpatterns = [
    path("", views.home, name="home"),
]
