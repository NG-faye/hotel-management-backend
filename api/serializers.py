from rest_framework import serializers
from django.contrib.auth.models import User
from djoser.serializers import UserCreateSerializer

class UserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name')

    def create(self, validated_data):
        # On s'assure que username est présent
        if not validated_data.get('username'):
            validated_data['username'] = validated_data.get('email')
            
        # On utilise create_user avec les arguments déballés
        return User.objects.create_user(**validated_data)