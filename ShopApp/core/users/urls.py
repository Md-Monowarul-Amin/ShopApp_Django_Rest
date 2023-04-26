# todo/todo_api/urls.py : API urls.py
from django.urls import path, include

from .views import (
    RegisterUserView
)

urlpatterns = [
    path('', RegisterUserView.as_view()),
]