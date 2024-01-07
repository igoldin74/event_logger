from rest_framework import serializers
from event_logger_app.models import EventEntry, Event

class EventEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventEntry
        fields = ["event", "client_ip", "timestamp"]


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["name", "event_timestamp"]