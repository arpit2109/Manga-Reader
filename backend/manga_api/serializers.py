# File: backend/manga_api/serializers.py
from rest_framework import serializers
from .models import User, Tag, Manga, Chapter, Comment, Bookmark, ViewLog

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ['id', 'title', 'chapter_number', 'images', 'uploaded_at']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'text', 'timestamp']

class MangaSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    chapters = ChapterSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    is_bookmarked = serializers.SerializerMethodField()

    class Meta:
        model = Manga
        fields = ['id', 'title', 'description', 'cover_image', 'tags', 'chapters', 'comments', 'is_bookmarked']

    def get_is_bookmarked(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return obj.bookmarked_by.filter(user=user).exists()
        return False

class BookmarkSerializer(serializers.ModelSerializer):
    manga = MangaSerializer(read_only=True)

    class Meta:
        model = Bookmark
        fields = ['id', 'manga', 'created_at']
