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
from djoser.serializers import UserCreateSerializer

# 1. On garde ton nom
class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

# 2. On garde ton nom 'UserSerializer' pour que 'views.py' le trouve
class UserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'password', 'first_name')

    def validate(self, attrs):
        # On force le username à être l'email pour éviter l'erreur
        attrs['username'] = attrs.get('email')
        return super().validate(attrs)