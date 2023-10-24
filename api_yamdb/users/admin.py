from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import UserModel

UserAdmin.fieldsets += (
    ('Extra Fields', {'fields': ('bio',)}),
)

admin.site.register(UserModel, UserAdmin)
