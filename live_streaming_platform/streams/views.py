from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Stream
from .serializers import StreamSerializer

class StreamViewSet(viewsets.ModelViewSet):
    queryset = Stream.objects.all()
    serializer_class = StreamSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
