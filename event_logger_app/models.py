from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Event(models.Model):
    """An event that occurs and being logged"""
    name = models.CharField(max_length=200)
    event_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """return a self representation of an event"""
        return self.name


class EventEntry(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    #user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, 
                                #default="admin", blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return "Name: "+ self.event.name + " Created By: " + str(self.user) + " Date: " + str(self.timestamp)