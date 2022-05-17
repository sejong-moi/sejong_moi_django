
from django.urls import path
from . import views


from login_api.views import *

app_name = "login_api"

urlpatterns = [
    path('list', views.list, name='list'),
    # path("logout", views.logout_view, name="logout"),
]
