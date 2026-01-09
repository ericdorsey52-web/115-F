"""
Models for the Manga Creators community.
"""
from django.db import models
from django.contrib.auth.models import User


class MangaPost(models.Model):
    """Model for manga/anime character discussion posts."""
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='posts/', blank=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
