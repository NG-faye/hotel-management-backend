# OPTION 2 (RECOMMANDÉE) : Hérite du serializer Djoser

from djoser.serializers import UserCreateSerializer as DjoserUserCreateSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Hotel

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

# ✅ Hérite du serializer Djoser qui gère déjà l'activation
class UserSerializer(DjoserUserCreateSerializer):
    class Meta(DjoserUserCreateSerializer.Meta):
        model = User
        fields = ('id', 'username', 'email', 'password', 're_password', 'first_name')
        extra_kwargs = {
            'username': {'required': False},
            'email': {'required': True},
        }
    
    def create(self, validated_data):
        # Ajoute l'email comme username si pas fourni
        if not validated_data.get('username'):
            validated_data['username'] = validated_data.get('email')
        
        # Laisse Djoser gérer la création + envoi d'email
        return super().create(validated_data)