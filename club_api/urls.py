
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *


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
    path('is_interested', is_interested),
    path('add_interested', add_interested),
    path('del_interested', del_interested),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)