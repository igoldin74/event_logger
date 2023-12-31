from django.contrib import admin

# Register your models here.
from event_logger_app.models import Event, EventEntry

admin.site.register(Event)
admin.site.register(EventEntry)