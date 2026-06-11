from rest_framework import serializers
from .models import Registration
from app.events.models import Event

class RegistrationListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    event = serializers.CharField(source='event.title', read_only=True)

    class Meta:
        model = Registration
        fields = ['id', 'user', 'event', 'registered_at', 'status']

class RegistrationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['event'] # user va status avtomatik olinadi/qo'yiladi

    def validate(self, attrs):
        event = attrs.get('event')
        
        # Tadbir faol ekanligini tekshirish
        if not event.is_active:
            raise serializers.ValidationError("Bu tadbir hozirda faol emas.")

        # Joy qolganligini tekshirish (So'nggi vazifa sharti)
        current_registrations = Registration.objects.filter(event=event, status='confirmed').count()
        if current_registrations >= event.capacity:
            raise serializers.ValidationError("Tadbirda joy qolmagan (capacity to'lgan)!")
            
        return attrs