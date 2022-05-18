
from django.urls import path
from . import views


from login_api.views import *

app_name = "login_api"

urlpatterns = [
    path('list', views.list, name='list'),
    path('list_show', views.list_show, name='list_show'),
    path('list_cluture', views.list_cluture, name='list_cluture'),
    path('list_voluteer', views.list_voluteer, name='list_voluteer'),
    path('list_religion', views.list_religion, name='list_religion'),
    path('list_athletic', views.list_athletic, name='list_athletic'),
    path('list_academic', views.list_academic, name='list_academic'),
]
