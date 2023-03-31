from django.contrib import admin
from django.urls import path
from tasks.views import ListCreateTaskView, UpdateDestroyTaskView

urlpatterns = [
    path("", ListCreateTaskView.as_view()),
    path("task-detail/<str:pk>", UpdateDestroyTaskView.as_view()),
]