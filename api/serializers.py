# from rest_framework import serializers
# from .models import Hotel
# from django.contrib.auth.models import User
# from djoser.serializers import UserCreateSerializer as DjoserUserCreateSerializer


# # Serializer pour les Hôtels
# class HotelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Hotel
#         fields = '__all__'

# # Serializer pour l'Inscription (Utilisateur)
# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'password')
#         # On rend l'email obligatoire
#         extra_kwargs = {'email': {'required': True}}

#     def create(self, validated_data):
#         # STRATÉGIE : On utilise l'email fourni pour remplir le champ username
#         # Comme ça, l'utilisateur se connecte avec son mail.
#         user = User.objects.create_user(
#             username=validated_data['email'], # <--- L'email devient l'identifiant
#             email=validated_data['email'],
#             password=validated_data['password']
#         )
#         return user


from rest_framework import serializers
from .models import Hotel
from django.contrib.auth.models import User
from djoser.serializers import UserCreateSerializer as DjoserUserCreateSerializer

# 1. Serializer pour les Hôtels (Inchangé)
class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

# 2. Le VRAI Serializer pour l'Inscription (Correction Djoser)
class CustomUserCreateSerializer(DjoserUserCreateSerializer):
    class Meta(DjoserUserCreateSerializer.Meta):
        model = User
        # On définit les champs que ton Frontend envoie
        fields = ('id', 'email', 'password', 'first_name')

    def validate(self, attrs):
        # Cette ligne est la clé : elle crée le 'username' à partir de l'email
        # juste avant que Django ne valide les données.
        attrs['username'] = attrs.get('email')
        return super().validate(attrs)