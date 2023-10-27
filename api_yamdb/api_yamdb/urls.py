from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from users.views import CreateTokenView, GetTokenView, UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
    path('api/v1/auth/signup/', CreateTokenView.as_view()),
    path('api/v1/auth/token/', GetTokenView.as_view()),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include('api.urls')),
]
