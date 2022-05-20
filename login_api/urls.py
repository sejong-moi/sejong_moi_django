
from django.urls import path
from .views import LoginView, UserView, LogoutView


app_name = "login_api"

urlpatterns = [
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
]

'''

from django.urls import path
from . import views


from login_api.views import *

app_name = "login_api"

urlpatterns = [
    path('helloapi', views.helloApi),
    path('login', views.login, name='login'),
    # path("logout", views.logout_view, name="logout"),
]

'''