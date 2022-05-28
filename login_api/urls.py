
from django.urls import path
from .views import LoginView, UserView, LogoutView


app_name = "login_api"

urlpatterns = [
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
]
