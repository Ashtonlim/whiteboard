from vidboard.models import Video
from rest_framework import viewsets, permissions
from .serializers import VideoSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = VideoSerializer