from rest_framework import serializers
from .models import Hotel
from django.contrib.auth.models import User
from djoser.serializers import UserCreateSerializer

# 1. Serializer pour les Hôtels (Rétabli pour corriger l'ImportError)
class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

# 2. Serializer pour l'Utilisateur (Configuré pour éviter l'erreur de username)
class UserSerializer(UserCreateSerializer):
    username = serializers.CharField(required=False, allow_blank=True)

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name')

    def create(self, validated_data):
        # On récupère l'email pour l'utiliser comme nom d'utilisateur
        email = validated_data.get('email')
        
        # On force le username dans les données avant la création
        validated_data['username'] = email
        
        # On utilise la méthode officielle de Django pour créer l'utilisateur
        return User.objects.create_user(**validated_data)