from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Hotel

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    re_password = serializers.CharField(write_only=True) # Ajouté pour correspondre à ton React

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 're_password', 'first_name')
        extra_kwargs = {
            'username': {'required': False},
            'email': {'required': True},
        }

    def validate(self, attrs):
        # On vérifie que les deux mots de passe sont identiques
        if attrs.get('password') != attrs.get('re_password'):
            raise serializers.ValidationError({"password": "Les mots de passe ne correspondent pas."})
        return attrs

    def create(self, validated_data):
        # On retire re_password avant la création
        validated_data.pop('re_password')
        
        # ON FORCE LE USERNAME ICI : C'est la solution à ton erreur
        email = validated_data.get('email')
        
        return User.objects.create_user(
            username=email, 
            email=email,
            password=validated_data.get('password'),
            first_name=validated_data.get('first_name', '')
        )