from rest_framework import viewsets, permissions, status, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail

from users.models import UserModel
from users.serializers import (
    UserTokenSerializer, UserSerializer, UserTokenCreateSerializer
)
from users.permissions import AdminUser, IsAuth


class CreateTokenView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = UserTokenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_mail(
                subject='Код подтверждения!',
                message=f'Ваш код: {serializer.instance.confirmation_code }',
                from_email='from@example.com',
                recipient_list=[f'{serializer.instance.email}'],
            )
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetTokenView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = UserTokenCreateSerializer(data=request.data)
        if serializer.is_valid():
            return Response({'token': serializer.validated_data.get('access')},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AdminUser,)
    filter_backends = (filters.SearchFilter,)
    pagination_class = PageNumberPagination
    search_fields = ('username',)

    def get_object(self):
        user = get_object_or_404(UserModel, username=self.kwargs['pk'])
        return user

    def update(self, request, *args, **kwargs):
        if self.action == 'update':
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().update(request, *args, **kwargs)

    @action(methods=['get', 'patch'], detail=False, url_path='me')
    def me(self, request):
        user = UserModel.objects.get(username=request.user.username)
        if request.method == 'GET':
            serializer = self.get_serializer(user)
            return Response(serializer.data)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validated_data['role'] = user.role
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_permissions(self):
        if '/me' in self.request.path:
            return (IsAuth(),)
        return super().get_permissions()
