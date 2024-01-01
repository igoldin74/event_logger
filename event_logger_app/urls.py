"""Defines URLs patterns for event_logger app."""

from django.urls import path 

from . import views


urlpatterns = [
    # Homepage:
    path('', views.index, name='index'),
    # Event entries:
    path('event_entries/', views.event_entries, name='event_entries'),
]