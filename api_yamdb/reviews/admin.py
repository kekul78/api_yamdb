from django.contrib import admin

from .models import Category, Comment, Title, Genre, GenreTitle, Review


@admin.register(Category, Comment, Title, Genre, GenreTitle, Review)
class BlogAdmin(admin.ModelAdmin):
    pass
