# File: backend/manga_api/views.py
from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from manga_api.models import Tag, Manga, Chapter, Comment, Bookmark, ViewLog
from manga_api.serializers import TagSerializer, MangaSerializer, ChapterSerializer, CommentSerializer, BookmarkSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class MangaViewSet(viewsets.ModelViewSet):
    queryset = Manga.objects.prefetch_related('tags', 'chapters', 'comments')
    serializer_class = MangaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'tags__name']

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def bookmark(self, request, pk=None):
        manga = self.get_object()
        Bookmark.objects.get_or_create(user=request.user, manga=manga)
        return Response({'status': 'bookmarked'})

    @action(detail=False, methods=['get'])
    def top_hits(self, request):
        # Return top 10 manga by view count
        manga_ids = ViewLog.objects.values('manga').annotate(count=models.Count('id')).order_by('-count')[:10]
        mangas = Manga.objects.filter(id__in=[m['manga'] for m in manga_ids])
        serializer = MangaSerializer(mangas, many=True, context={'request': request})
        return Response(serializer.data)

class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookmarkViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BookmarkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Bookmark.objects.filter(user=self.request.user)

from django.shortcuts import render

def root_view(request):
    return render(request, 'home.html')


from django.shortcuts import render
from django.contrib.auth.models import AnonymousUser

def home_view(request):
    if request.user.is_authenticated:
        context = {
            "user": request.user,
            "is_logged_in": True
        }
    else:
        context = {
            "error": "You are not logged in.",
            "is_logged_in": False
        }
    return render(request, "home.html", context)
