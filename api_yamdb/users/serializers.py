from rest_framework import serializers
from users.models import UserModel
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from django.core.validators import RegexValidator


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('username', 'email', 'first_name', 'last_name', 'bio', 'role')
        read_only_fields = ('password',)
        model = UserModel


class UserTokenSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=254, required=True)
    username = serializers.CharField(max_length=150, required=True,
                                     validators=[RegexValidator(
                                         r'^[\w.@+-]+\Z')])

    def validate_username(self, value):
        print('value')
        if value == 'me':
            raise serializers.ValidationError(
                'Некорректное имя пользователя!')
        return value

    def validate(self, data):
        if not (bool(UserModel.objects.filter(username=data['username']))
                == bool(UserModel.objects.filter(email=data['email']))):
            raise serializers.ValidationError(
                '!!!')
        return data

    def create(self, validated_data):
        confirmation_code = '123'
        validated_data['confirmation_code'] = confirmation_code
        if UserModel.objects.filter(username=validated_data['username']):
            return UserModel.objects.get(username=validated_data['username'])
        else:
            user = UserModel.objects.create(**validated_data)
            return user


class UserTokenCreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=128)
    confirmation_code = serializers.CharField(max_length=128)

    def validate(self, data):
        user = get_object_or_404(UserModel, username=data['username'])
        confirmation_code = user.confirmation_code
        if data['confirmation_code'] != confirmation_code:
            raise serializers.ValidationError(
                'Неправильный пароль!')
        refresh = RefreshToken.for_user(user)
        print(refresh.access_token)
        data["access"] = str(refresh.access_token)
        return data
