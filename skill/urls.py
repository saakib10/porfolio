from . import views
from django.urls import path

urlpatterns = [
    path('skills/',views.show_skill, name = "skills")
]