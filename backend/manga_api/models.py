# File: backend/manga_api/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

# User model
class User(AbstractUser):
    pass

# Tags for each manga
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Manga model
class Manga(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='manga_covers/')
    tags = models.ManyToManyField(Tag, related_name='manga')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Chapter model
class Chapter(models.Model):
    manga = models.ForeignKey(Manga, related_name='chapters', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    chapter_number = models.IntegerField()
    images = models.ImageField(upload_to='chapters/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.manga.title} - Chapter {self.chapter_number}"

# Comment model
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    manga = models.ForeignKey(Manga, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.manga.title}"

# Bookmark model
class Bookmark(models.Model):
    user = models.ForeignKey(User, related_name='bookmarks', on_delete=models.CASCADE)
    manga = models.ForeignKey(Manga, related_name='bookmarked_by', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'manga')

# Manga view logs
class ViewLog(models.Model):
    manga = models.ForeignKey(Manga, related_name='views', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


