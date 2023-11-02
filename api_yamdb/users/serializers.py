from rest_framework import serializers

from users.models import UserModel
from users.validators import validate_forbidden_username


MAX_LENGTH = 150


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор модели User."""
    class Meta:
        fields = ('username', 'email', 'first_name',
                  'last_name', 'bio', 'role')
        read_only_fields = ('password',)
        model = UserModel


class UserTokenSerializer(serializers.Serializer):
    """Сериализатор запроса на получение кода подтверждения."""
    email = serializers.EmailField(max_length=MAX_LENGTH, required=True)
    username = serializers.CharField(max_length=MAX_LENGTH, required=True,
                                     validators=[validate_forbidden_username])

    def validate(self, data):
        """Проверка при введении правильного ника или почты."""
        if (bool(UserModel.objects.filter(username=data['username']))
                and not bool(UserModel.objects.filter(email=data['email']))):
            raise serializers.ValidationError(
                'Ошибка, проверьте правильность почты!')
        elif (not bool(UserModel.objects.filter(username=data['username']))
              and bool(UserModel.objects.filter(email=data['email']))):
            raise serializers.ValidationError(
                'Ошибка, проверьте правильность логина!')
        return data


class UserTokenCreateSerializer(serializers.Serializer):
    """Сериализатор запроса на получение токена."""
    username = serializers.CharField(max_length=MAX_LENGTH)
    confirmation_code = serializers.CharField(max_length=MAX_LENGTH)
