from django.shortcuts import render
from .models import EventEntry

# Create your views here.

def index(request):
    """Homepage"""
    return render(request, 'event_logger_app/index.html')

def event_entries(request):
    """Show all event entries"""
    event_entries = EventEntry.objects.order_by('timestamp')
    # Storing result set in a dictionary:
    context = {'event_entries' : event_entries}
    return render(request, 'event_logger_app/event_entries.html', context)