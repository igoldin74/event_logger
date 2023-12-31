from django.db import models

# Create your models here.
class Event(models.Model):
    """An event that occurs and being logged"""
    event_type = models.CharField(max_length=200)
    event_timestamp = models.DateTimeField(auto_now_add=True)

def __str__(self):
    """return a self representation of an event"""
    return self.event_type
