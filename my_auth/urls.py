from django.urls import path
from . import views


urlpatterns = [
    path(r'login', views.LoginView.as_view()),
    path(r'register', views.RegisterView.as_view()),
]
