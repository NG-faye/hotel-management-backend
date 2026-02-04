from djoser.serializers import UserCreateSerializer as DjoserUserCreateSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Hotel

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

# ✅ Version finale qui fonctionne
class UserSerializer(DjoserUserCreateSerializer):
    class Meta(DjoserUserCreateSerializer.Meta):
        model = User
        # ✅ On garde les champs du parent Djoser + on ajoute nos customisations
        fields = tuple(DjoserUserCreateSerializer.Meta.fields) + ('first_name',)
        extra_kwargs = {
            'username': {'required': False},
            'email': {'required': True},
        }
    
    def create(self, validated_data):
        # Ajoute l'email comme username si pas fourni
        if not validated_data.get('username'):
            validated_data['username'] = validated_data.get('email')
        
        # Laisse Djoser gérer tout (création + validation re_password + envoi email)
        return super().create(validated_data)