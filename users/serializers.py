from django.conf import settings
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

from users.models import User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Добавление пользовательских полей в токен
        token['username'] = user.username
        token['telegram'] = user.telegram

        return token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('telegram', 'password',)

    def create(self, validated_data):
        user = User.objects.create(
            telegram=validated_data['telegram'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
