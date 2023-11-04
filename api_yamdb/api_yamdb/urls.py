from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from users.views import CreateTokenView, GetTokenView

auth_patern = [
    path('signup/', CreateTokenView.as_view()),
    path('token/', GetTokenView.as_view()),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
    path('api/v1/auth/', include(auth_patern)),
    path('api/v1/', include('api.urls')),
]
