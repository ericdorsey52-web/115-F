"""
Django admin configuration for manga_app.
"""
from django.contrib import admin
from .models import MangaPost


@admin.register(MangaPost)
class MangaPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'author')
