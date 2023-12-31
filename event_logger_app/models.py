from django.db import models

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
    client_ip = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.event.name
    

