from django.urls import path
from shopauth import views

urlpatterns = [
    path("signup/",views.sign_up, name='signup')
]