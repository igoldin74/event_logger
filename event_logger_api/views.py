from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from event_logger_app.models import EventEntry
from .serializers import EventEntrySerializer

class EventEntryApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the event entry items ordered by timestamp
        '''
        entries = EventEntry.objects.order_by('timestamp')
        serializer = EventEntrySerializer(entries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'event': request.data.get('event'), 
            'client_ip': request.data.get('client_ip')
        }
        serializer = EventEntrySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
