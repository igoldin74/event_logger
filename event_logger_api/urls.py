"""Defines URLs patterns for event_logger_api app."""

from django.urls import path 

from .views import ( EventEntryApiView,)


urlpatterns = [
    path('api', EventEntryApiView.as_view()),
]