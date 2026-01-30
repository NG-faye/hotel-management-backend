from rest_framework import serializers
from .models import Hotel
from django.contrib.auth.models import User
from djoser.serializers import UserCreateSerializer

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class UserSerializer(UserCreateSerializer):
    # On définit explicitement le champ username comme n'étant pas requis dans le JSON
    # mais on va le remplir nous-mêmes.
    username = serializers.CharField(required=False, allow_blank=True)

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name')

    def create(self, validated_data):
        # Si le frontend n'envoie pas de username, on prend l'email
        if 'username' not in validated_data or not validated_data['username']:
            validated_data['username'] = validated_data.get('email')
        
        # On utilise la méthode de création d'utilisateur de Django directement
        return User.objects.create_user(**validated_data)