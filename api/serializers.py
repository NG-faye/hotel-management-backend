from djoser.serializers import UserCreateSerializer as DjoserUserCreateSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Hotel

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

# ✅ Version corrigée
class UserSerializer(DjoserUserCreateSerializer):
    # On déclare re_password ici, mais pas dans fields
    re_password = serializers.CharField(write_only=True, required=True)
    
    class Meta(DjoserUserCreateSerializer.Meta):
        model = User
        # ⚠️ NE PAS mettre 're_password' ici car ce n'est pas un champ du modèle User
        fields = ('id', 'username', 'email', 'password', 'first_name')
        extra_kwargs = {
            'username': {'required': False},
            'email': {'required': True},
        }
    
    def validate(self, attrs):
        # Validation du re_password
        if attrs.get('password') != attrs.get('re_password'):
            raise serializers.ValidationError({"password": "Les mots de passe ne correspondent pas."})
        return attrs
    
    def create(self, validated_data):
        # Enlève re_password avant la création
        validated_data.pop('re_password', None)
        
        # Ajoute l'email comme username si pas fourni
        if not validated_data.get('username'):
            validated_data['username'] = validated_data.get('email')
        
        # Laisse Djoser gérer la création + envoi d'email
        return super().create(validated_data)