from rest_framework import serializers
from .models import Hotel
from django.contrib.auth.models import User

# Serializer pour les Hôtels
class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

# Serializer pour l'Inscription (Utilisateur)
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        # On rend l'email obligatoire
        extra_kwargs = {'email': {'required': True}}

    def create(self, validated_data):
        # STRATÉGIE : On utilise l'email fourni pour remplir le champ username
        # Comme ça, l'utilisateur se connecte avec son mail.
        user = User.objects.create_user(
            username=validated_data['email'], # <--- L'email devient l'identifiant
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user