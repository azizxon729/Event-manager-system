from rest_framework import viewsets, serializers
from rest_framework.permissions import IsAuthenticated
from .models import Registration
from .serializers import RegistrationListSerializer, RegistrationCreateSerializer

class RegistrationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):


        return Registration.objects.filter(user=self.request.user)

    def get_serializer_class(self):


        if self.action == 'list':
            return RegistrationListSerializer
        return RegistrationCreateSerializer

    def perform_create(self, serializer):

        serializer.save(user=self.request.user, status='confirmed')

    def create(self, request, *args, **kwargs):
     


        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        event = serializer.validated_data.get('event')
        
        current_registrations_count = Registration.objects.filter(event=event).count()
        
        if current_registrations_count >= event.capacity:
            raise serializers.ValidationError(
                {"error": "Tadbirda joy qolmagan (capacity to'lgan)!"}
            )
            
        # Agar joy bo'lsa, standart yaratish jarayonini davom ettiramiz
        return super().create(request, *args, **kwargs)