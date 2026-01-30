from rest_framework import serializers
from .models import Hotel
from django.contrib.auth.models import User
from djoser.serializers import UserCreateSerializer

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class UserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name')
        extra_kwargs = {
            'username': {'required': False, 'allow_blank': True},
        }

    def create(self, validated_data):
        # On extrait les données manuellement
        email = validated_data.get('email')
        password = validated_data.get('password')
        first_name = validated_data.get('first_name', '')

        # ON FORCE LA CRÉATION MANUELLE SANS PASSER PAR LE MANAGER CLASSIQUE
        user = User.objects.create(
            username=email, # Le username EST l'email
            email=email,
            first_name=first_name,
            is_active=False # Important pour l'activation par mail
        )
        user.set_password(password) # On crypte le mot de passe
        user.save()
        return user