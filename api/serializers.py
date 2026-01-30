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
        # On demande explicitement ces champs
        fields = ('id', 'email', 'password', 'first_name')

    def create(self, validated_data):
        # On récupère l'email
        email = validated_data.get('email')
        # On force le username à être l'email AVANT la création
        validated_data['username'] = email
        # On appelle la méthode de création de Djoser avec le username inclus
        return super().create(validated_data)