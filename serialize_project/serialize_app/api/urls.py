from django.urls import path
from .api import StudentAPI

urlpatterns = [
    path('student/',StudentAPI.as_view()),
]