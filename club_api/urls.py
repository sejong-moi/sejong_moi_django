
from django.urls import path


from .views import *

app_name = "login_api"

urlpatterns = [
    path('club/<str:name>', club, name='club'),
    path('list', list, name='list'),
    path('list_show', list_show, name='list_show'),
    path('list_cluture', list_cluture, name='list_cluture'),
    path('list_voluteer', list_voluteer, name='list_voluteer'),
    path('list_religion', list_religion, name='list_religion'),
    path('list_athletic', list_athletic, name='list_athletic'),
    path('list_academic', list_academic, name='list_academic'),
    path('register', register_club),
]
