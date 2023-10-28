from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from django.core.validators import RegexValidator

from users.models import UserModel

import random


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор модели User."""
    class Meta:
        fields = ('username', 'email', 'first_name',
                  'last_name', 'bio', 'role')
        read_only_fields = ('password',)
        model = UserModel


class UserTokenSerializer(serializers.Serializer):
    """Сериализатор запроса на получение кода подтверждения."""
    email = serializers.EmailField(max_length=254, required=True)
    username = serializers.CharField(max_length=150, required=True,
                                     validators=[RegexValidator(
                                         r'^[\w.@+-]+\Z')])

    def validate_username(self, value):
        """Проверка неразрешенного имени."""
        if value == 'me':
            raise serializers.ValidationError(
                'Некорректное имя пользователя!')
        return value

    def validate(self, data):
        """Проверка наличия имени или почты в базе данных."""
        if not (bool(UserModel.objects.filter(username=data['username']))
                == bool(UserModel.objects.filter(email=data['email']))):
            raise serializers.ValidationError(
                'Ошибка, проверьте почти или никнейм!')
        return data

    def create(self, validated_data):
        """Создание кода подтверждения и пользователя."""
        confirmation_code = random.randint(100000, 999999)
        validated_data['confirmation_code'] = confirmation_code
        # Проверка на присутствие пользователя в базе данных.
        if UserModel.objects.filter(username=validated_data['username']):
            user = UserModel.objects.get(username=validated_data['username'])
            user.confirmation_code = confirmation_code
            user.save()
            return user
        else:
            user = UserModel.objects.create(**validated_data)
            return user


class UserTokenCreateSerializer(serializers.Serializer):
    """Сериализатор запроса на получение токена."""
    username = serializers.CharField(max_length=128)
    confirmation_code = serializers.CharField(max_length=128)

    def validate(self, data):
        user = get_object_or_404(UserModel, username=data['username'])
        confirmation_code = user.confirmation_code
        if data['confirmation_code'] != confirmation_code:
            raise serializers.ValidationError(
                'Неправильный пароль!')
        refresh = RefreshToken.for_user(user)
        data["access"] = str(refresh.access_token)
        return data
