from django.contrib import admin
from django.urls import path
from tasks.views import HomeView

urlpatterns = [
    path("", HomeView.as_view()),
]