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
        # On inclut 'username' dans les champs pour que Django ne râle pas
        fields = ('id', 'username', 'email', 'password', 'first_name')

    def validate(self, attrs):
        # STRATÉGIE CRUCIALE : 
        # Si le username n'est pas envoyé ou est vide, on lui donne la valeur de l'email
        if not attrs.get('username'):
            attrs['username'] = attrs.get('email')
        return super().validate(attrs)