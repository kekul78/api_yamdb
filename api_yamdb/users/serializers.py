from rest_framework import serializers

from users.models import UserModel
from users.validators import validate_forbidden_username
import users.constants as const


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор модели User."""
    class Meta:
        fields = ('username', 'email', 'first_name',
                  'last_name', 'bio', 'role')
        read_only_fields = ('password',)
        model = UserModel


class UserTokenSerializer(serializers.Serializer):
    """Сериализатор запроса на получение кода подтверждения."""
    email = serializers.EmailField(max_length=const.MAX_LENGTH, required=True)
    username = serializers.CharField(max_length=const.MAX_LENGTH,
                                     required=True,
                                     validators=[validate_forbidden_username])

    def validate(self, data):
        """Проверка при введении правильного ника или почты."""
        # Валидация совокупности двух полей (1 и 0; 0 и 1)
        if (UserModel.objects.filter(username=data['username']).exists()
                and not UserModel.objects
                .filter(email=data['email']).exists()):
            raise serializers.ValidationError(
                'Ошибка, проверьте правильность почты!')
        elif (not UserModel.objects.filter(username=data['username']).exists()
              and UserModel.objects.filter(email=data['email']).exists()):
            raise serializers.ValidationError(
                'Ошибка, проверьте правильность логина!')
        return data


class UserTokenCreateSerializer(serializers.Serializer):
    """Сериализатор запроса на получение токена."""
    username = serializers.CharField(max_length=const.MAX_LENGTH)
    confirmation_code = serializers.CharField(max_length=const.MAX_LENGTH)
