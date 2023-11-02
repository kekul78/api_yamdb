from django.contrib import admin

from .models import UserModel


@admin.register(UserModel)
class BlogAdmin(admin.ModelAdmin):
    pass
