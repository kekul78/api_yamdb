from rest_framework import serializers
from users.models import UserModel


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = UserModel
