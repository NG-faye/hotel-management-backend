from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Hotel

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    re_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 're_password', 'first_name')
        extra_kwargs = {
            'username': {'required': False},
            'email': {'required': True},
        }

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('re_password'):
            raise serializers.ValidationError({"password": "Les mots de passe ne correspondent pas."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('re_password')
        email = validated_data.get('email')
        
        # On crée l'utilisateur inactif
        user = User.objects.create_user(
            username=email, 
            email=email,
            password=validated_data.get('password'),
            first_name=validated_data.get('first_name', ''),
            is_active=False
        )
        
        # Le return doit être ICI, aligné sous 'user ='
        return user
    


    