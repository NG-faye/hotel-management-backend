from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Hotel
from djoser.serializers import UserCreateSerializer

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class UserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        # On inclut explicitement username ici pour que Django soit content
        fields = ('id', 'username', 'email', 'password', 'first_name')
        extra_kwargs = {
            'username': {'required': False},
            'email': {'required': True},
        }

    def validate(self, attrs):
        # On force le username à prendre la valeur de l'email AVANT la validation
        if 'email' in attrs:
            attrs['username'] = attrs['email']
        return super().validate(attrs)

    def create(self, validated_data):
        # On s'assure une dernière fois que le username est là
        if 'username' not in validated_data:
            validated_data['username'] = validated_data.get('email')
        return super().create(validated_data)