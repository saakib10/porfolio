from django.urls import path
from . import views

urlpatterns = [
    path('works/',views.work_show,name='workshow')
]