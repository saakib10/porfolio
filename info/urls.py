from django.urls import path
from . import views

urlpatterns = [
    path('infoo/',views.info_show , name = 'infoshow')
]