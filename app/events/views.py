from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import Event
from .serializers import EventListSerializer, EventDetailSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return EventListSerializer
        return EventDetailSerializer

    def get_permissions(self):
        # Faqat admin tadbir yarata oladi, o'chira oladi yoki o'zgartira oladi
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return [AllowAny()]